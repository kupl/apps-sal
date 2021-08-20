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
    while y:
        (x, y) = (y, x % y)
    return x


mm = 1000000007


def solve():
    t = 1
    for it in range(t):
        n = nu()
        a = input()
        cc = 0
        for i in range(n):
            if int(a[i]) % 2 == 0:
                cc += i + 1
        print(cc)


def __starting_point():
    solve()


__starting_point()
