from math import *


def r1(t):
    return t(input())


def r2(t):
    return [t(i) for i in input().split()]


def r3(t):
    return [t(i) for i in input()]


for _ in range(r1(int)):
    b = input()
    a = ''
    for i in range(0, len(b) + 1, 2):
        a += b[min(i, len(b) - 1)]
    print(a)
