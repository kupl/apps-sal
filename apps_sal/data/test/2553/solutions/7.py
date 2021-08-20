from math import *


def r1(t):
    return t(input().strip())


def r2(t):
    return [t(i) for i in input().strip().split()]


def r3(t):
    return [t(i) for i in input().strip()]


for _ in range(int(input())):
    (n, x) = r2(int)
    a = r2(int)
    co = 0
    ce = 0
    for i in a:
        if i % 2 == 0:
            ce += 1
        else:
            co += 1
    if x == n and co % 2 == 0 or co <= 0 or (ce == 0 and x % 2 == 0):
        print('No')
    else:
        print('Yes')
