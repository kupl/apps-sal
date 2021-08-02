import sys
from math import *


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


n = mint()
a = []
for i in mints():
    if len(a) > 0 and a[-1] == i:
        a[-1] += 1
        while len(a) > 1 and a[-2] == a[-1]:
            a.pop()
            a[-1] += 1
    else:
        a.append(i)
print(len(a))
print(*a)
