import io
import sys
import atexit
import os

import math as ma
from decimal import Decimal as dec
from itertools import permutations


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


mm = 1000000007


def solve():
    t = 1
    for it in range(t):
        n = nu()
        s = list(input())
        if(n % 2 == 1):
            print(":(")
        else:
            gg = 0
            for i in range(n):
                if(s[i] == "("):
                    gg += 1
            if(gg > n // 2):
                print(":(")
                continue
            dd = n // 2 - gg
            for i in range(n):
                if(s[i] == "?"):
                    if(dd > 0):
                        s[i] = "("
                        dd -= 1
                    else:
                        s[i] = ")"
            xc = [0] * n
            ss = 0
            for i in range(n):
                if(s[i] == "("):
                    ss += 1
                else:
                    ss -= 1
                xc[i] = ss
            fl = True
            for i in range(n - 1):
                if(xc[i] <= 0):
                    fl = False
            if(xc[n - 1] != 0):
                fl = False
            if(fl):
                for i in range(n):
                    print(s[i], end="")
                print()
            else:
                print(":(")


def __starting_point():
    solve()


__starting_point()
