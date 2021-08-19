import sys
import string
from math import gcd
import getpass
import math
from decimal import Decimal


def ria():
    return [int(i) for i in input().split()]


if getpass.getuser() != 'frohenk':
    filename = 'half'
else:
    sys.stdin = open('input.txt')
(w, h, k) = ria()
suma = 0
for i in range(k):
    suma += w * 2 + h * 2 - 4
    w -= 4
    h -= 4
print(suma)
