import io
import sys
import atexit
import os
import math as ma
from decimal import Decimal as dec
from itertools import permutations
from itertools import combinations


def li():
    return list(map(int, input().split()))


def num():
    return map(int, input().split())


def nu():
    return int(input())


def find_gcd(x, y):
    while (y):
        x, y = y, x % y
    return x


def lcm(x, y):
    gg = find_gcd(x, y)
    return (x * y // gg)


mm = 1000000007
yp = 0


def solve():
    t = 1
    for tt in range(t):
        n, m = num()
        a = [0] * n
        xx = []
        fl = True
        b = [0] * n
        for i in range(n):
            a[i] = li()
            b[i] = [0] * m
        for i in range(n - 1):
            for j in range(m - 1):
                if(a[i][j] == 1 and a[i][j + 1] == 1 and a[i + 1][j] == 1 and a[i + 1][j + 1] == 1):
                    xx.append((i, j))
                    b[i][j] = 1
                    b[i][j + 1] = 1
                    b[i + 1][j] = 1
                    b[i + 1][j + 1] = 1
        for i in range(n):
            for j in range(m):
                if(a[i][j] != b[i][j]):
                    fl = False
        if(fl):
            print(len(xx))
            for i in range(len(xx)):
                print(xx[i][0] + 1, xx[i][1] + 1)
        else:
            print(-1)


def __starting_point():
    solve()


__starting_point()
