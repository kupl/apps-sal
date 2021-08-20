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
    return list(map(int, sys.stdin.readline().split()))


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


def solve():
    t = nu()
    for tt in range(t):
        n = nu()
        s = input()
        mn = 1
        val = s
        for i in range(2, n + 1):
            x = s[0:i - 1]
            y = s[i - 1:]
            op = n - i + 1
            if op % 2 == 0:
                up = y + x
            else:
                up = y + x[::-1]
            if up < val:
                val = up
                mn = i
        print(val)
        print(mn)


def __starting_point():
    solve()


__starting_point()
