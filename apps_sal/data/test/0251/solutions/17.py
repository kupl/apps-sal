import math as ma
import sys
from decimal import Decimal as dec
from itertools import permutations


def li():
    return list(map(int, input().split()))


# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
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
    return map(int, input().split())


def nu():
    return int(input())


def find_gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


n, k = num()
h = li()
a = [0] * (max(h) + 5)
mx = max(h)
mn = min(h)
fo = True
for i in range(1, n):
    if(h[i] != h[i - 1]):
        fo = False
        break
for i in range(n):
    a[0] += 1
    a[h[i] + 1] -= 1
for i in range(1, len(a)):
    a[i] = a[i] + a[i - 1]
s = a[mx]
cc = 0
fl = False
for i in range(mx - 1, mn, -1):
    if(s + a[i] > k):
        fl = True
        s = a[i]
        cc += 1
    else:
        fl = False
        s += a[i]
if(s <= k and fo == False):
    cc += 1
print(cc)
