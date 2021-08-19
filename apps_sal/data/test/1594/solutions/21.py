import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


(n, m) = mints()
a = [0]
s = 0
for i in range(n):
    (c, t) = mints()
    s += c * t
    a.append(s)
j = 0
for i in mints():
    while not (i - 1 >= a[j] and i - 1 < a[j + 1]):
        j += 1
    print(j + 1)
