import io
import sys
import atexit
import os
import math as ma
from decimal import Decimal as dec
from itertools import permutations
from random import randint as rand


def li():
    return list(map(int, input().split()))


def num():
    return map(int, input().split())


def nu():
    return int(input())


def find_gcd(x, y):
    while y:
        (x, y) = (y, x % y)
    return x


def lcm(x, y):
    gg = find_gcd(x, y)
    return x * y // gg


mm = 1000000007
yp = 0


def solve():
    t = 1
    for _ in range(t):
        n = nu()
        x = [0] * n
        for i in range(n):
            x[i] = [0] * n
            pp = input()
            for j in range(n):
                if pp[j] == '.':
                    x[i][j] = 0
                else:
                    x[i][j] = 1
        while True:
            fl = False
            for i in range(n):
                for j in range(n):
                    if i - 1 >= 0 and i + 1 < n and (j - 1 >= 0) and (j + 1 < n):
                        if x[i][j] == 0 and x[i - 1][j] == 0 and (x[i + 1][j] == 0) and (x[i][j + 1] == 0) and (x[i][j - 1] == 0):
                            fl = True
                            x[i][j] = 1
                            x[i - 1][j] = 1
                            x[i + 1][j] = 1
                            x[i][j + 1] = 1
                            x[i][j - 1] = 1
                            break
                if fl:
                    break
            if fl == False:
                break
        pw = True
        for i in range(n):
            for j in range(n):
                if x[i][j] == 0:
                    pw = False
        if pw:
            print('YES')
        else:
            print('NO')


def __starting_point():
    solve()


__starting_point()
