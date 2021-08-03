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
    t = nu()
    for tt in range(t):
        n, m = num()
        a = [0] * n
        x = [0] * n
        y = [0] * m
        for i in range(n):
            p = input()
            a[i] = [0] * m
            for j in range(m):
                if(p[j] == "*"):
                    a[i][j] = 1
            x[i] = sum(a[i])
        for i in range(m):
            cc = 0
            for j in range(n):
                cc += a[j][i]
            y[i] = cc
        mn = 9999999999
        for i in range(n):
            for j in range(m):
                pp = 0
                pp = (n - x[i]) + (m - y[j])
                if(a[i][j] == 0):
                    pp -= 1
                mn = min(mn, pp)
        print(mn)


def __starting_point():
    solve()


__starting_point()
