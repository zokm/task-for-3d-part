from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_in_basket(browser):
    browser.get(link)
    time.sleep(5)
    button = WebDriverWait(browser, 6).until(EC.element_to_be_clickable(browser.find_element(By.CLASS_NAME, 'btn-add-to'
                                                                                                            '-basket')))
    assert button, "Button isn\'t clickable"
