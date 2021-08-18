import math as ma
import sys
from decimal import Decimal as dec
from itertools import permutations


def li():
    return list(map(int, input().split()))


def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        q = a // m
        t = m
        m = a % m
        a = t
        t = y
        y = x - q * y
        x = t
    if (x < 0):
        x = x + m0
    return x


def num():
    return list(map(int, input().split()))


def nu():
    return int(input())


def find_gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


l, r = num()
print("YES")
for i in range(l, r + 1, 2):
    print(i, i + 1)
