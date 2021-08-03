import sys
from collections import defaultdict
from copy import copy


def R(t=int): return t(input())
def RL(t=int): return [t(x) for x in input().split()]
def RLL(n, t=int): return [RL(t) for _ in range(n)]


def solve():
    n, x = RL()
    A = RL()
    A.sort(reverse=True)
    s = c = m = 0
    for a in A:
        s += a
        c += 1
        if s >= x * c:
            m = c
    print(m)


T = R()
for _ in range(T):
    solve()
