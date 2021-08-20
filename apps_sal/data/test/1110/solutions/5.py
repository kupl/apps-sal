import math
import sys


def buttons():
    n = int(input())
    rightbuttons = n
    wrongbuttons = (1 + n) * (n / 2) - n
    j = 1
    for i in range(n - 2, 0, -1):
        rightbuttons += j * i
        j += 1
    print(int(rightbuttons + wrongbuttons))


buttons()
