import math


def isMM(num):
    if num < 13 and num > 0:
        return True
    else:
        return False


def hantei(number):
    num = math.floor(number / 100)
    ber = number % 100
    if isMM(num) is False and isMM(ber) is False:
        return 'NA'
    elif isMM(num) is True and isMM(ber) is True:
        return 'AMBIGUOUS'
    elif isMM(num) is True and isMM(ber) is False:
        return 'MMYY'
    else:
        return 'YYMM'


num = int(input())
print(hantei(num))
