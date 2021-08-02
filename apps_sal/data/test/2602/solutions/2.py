from math import *


def r1(t):
    return t(input())


def r2(t):
    return [t(i) for i in input().split()]


for _ in range(r1(int)):
    a, b, n, m = r2(int)
    if n + m > a + b or m > min(a, b):
        print('No')
    else:
        print('Yes')
