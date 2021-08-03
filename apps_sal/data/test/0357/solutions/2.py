import math
import re
import os
import string
import sys


def ria():
    return [int(i) for i in input().split()]


def ri():
    return int(input())


def rfa():
    return [float(i) for i in input().split()]


eps = 1e-9


def is_equal(a, b):
    return abs(a - b) <= eps


def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)


st = input()
suma = st.count('Danil') + st.count('Olya') + st.count('Slava') + st.count('Ann') + st.count('Nikita')
print('YES' if suma == 1 else 'NO')
