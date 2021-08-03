from math import *


def r1(t):
    return t(input())


def r2(t):
    return [t(i) for i in input().split()]


for _ in range(r1(int)):
    n = r1(int)
    if n % 4 == 0:
        print('YES')
    else:
        print('NO')
