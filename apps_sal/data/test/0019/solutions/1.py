import sys
from math import gcd
from collections import defaultdict
from copy import copy


def R(t=int): return t(input())
def RL(t=int): return [t(x) for x in input().split()]
def RLL(n, t=int): return [RL(t) for _ in range(n)]


def solve():
    n = R()
    S = RLL(n)
    lp = lc = 0
    for p, c in S:
        if lp > p or lc > c or c - lc > p - lp:
            print('NO')
            return
        lp = p
        lc = c
    print('YES')


T = R()
for _ in range(T):
    solve()
