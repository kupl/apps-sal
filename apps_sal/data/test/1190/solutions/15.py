from math import *
import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


w1, h1, w2, h2 = mints()
s = w1 + w2 + (h1 + h2) * 2 + 4
print(s + abs(w1 - w2))
