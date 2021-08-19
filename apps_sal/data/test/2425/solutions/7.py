import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a


def stupid(x):
    r = 1
    for i in range(1, x):
        r = max(r, gcd(i & x, i ^ x))
    return r


d = dict()
d[511] = 73
d[2047] = 89
d[32767] = 4681
d[2097151] = 299593
d[8388607] = 178481
d[33554431] = 1082401


def smart(x):
    if x in d:
        return d[x]
    if x & x + 1 == 0:
        i = 0
        while (1 << i) - 1 != x:
            i += 1
        if i % 2 == 0:
            z = 0
            for i in range(0, i, 2):
                z += 1 << i
            return z
        else:
            return 1
    else:
        i = 1
        z = 0
        while i < x:
            if i & x == 0:
                z += i
            i *= 2
        return x + z


q = mint()
for i in range(q):
    x = mint()
    print(smart(x))
