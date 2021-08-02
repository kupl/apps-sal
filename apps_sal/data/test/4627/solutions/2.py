from math import *
import math


def r1(t):
    return t(input())


def r2(t):
    return [t(i) for i in input().split()]


for zzz in range(r1(int)):
    n = r1(int)
    a = r2(int)
    co = 0
    ce = 0
    for i in range(n):
        if a[i] & 1:
            co += 1
        else:
            ce += 1
    if (co % 2 == 0) and (ce % 2 == 0):
        print("YES")
    else:
        a.sort()
        ha = False
        for i in range(n - 1):
            if a[i + 1] - a[i] == 1:
                ha = True
                break
        if ha:
            print("YES")
        else:
            print("NO")
