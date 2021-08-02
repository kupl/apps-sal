import io
import sys
import atexit
import os
import math as ma
from decimal import Decimal as dec
from itertools import permutations
from itertools import combinations


def li():
    return list(map(int, sys.stdin.readline().split()))


def num():
    return map(int, sys.stdin.readline().split())


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
fact_powers = [0] * 19
tset = set()


def go(ind, x):
    if (ind == 19):
        tset.add(x)
        return

    if (x in tset):
        return
    go(ind + 1, x)
    i = 0
    for xx in fact_powers[ind]:
        p = x * xx
        if (p > 1e18):
            break
        go(ind + 1, p)


def solve():
    t = 1
    for tt in range(t):
        n = nu()
        a = li()
        b = li()
        i = 0
        j = 0
        s = set()
        cc = 0
        while(i < n and j < n):
            if(a[i] == b[j]):
                i += 1
                j += 1
            else:
                if(a[i] in s):
                    i += 1
                    continue
                s.add(b[j])
                cc += 1
                j += 1
        print(cc)


def __starting_point():
    solve()


__starting_point()
