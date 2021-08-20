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
        (n, k) = num()
        s = list(input())
        ol = [0] * (n + 1)
        move = 0
        last = 0
        ind = -1
        for i in range(n):
            if s[i] == '0':
                ox = i - last
                if k - ox >= 0:
                    k -= ox
                else:
                    ind = i
                    break
                last += 1
        if ind == -1:
            s.sort()
            print(*s, sep='')
        else:
            op = s[0:ind]
            oz = s[ind:]
            op.sort()
            op += oz
            while k > 0:
                (op[ind - 1], op[ind]) = (op[ind], op[ind - 1])
                ind -= 1
                k -= 1
            print(*op, sep='')


def __starting_point():
    solve()


__starting_point()
