import sys
from collections import defaultdict
from copy import copy


def R(t=int): return t(input())
def RL(t=int): return [t(x) for x in input().split()]
def RLL(n, t=int): return [RL(t) for _ in range(n)]


def solve():
    n = R()
    b = 1
    m = 1
    d = 0
    S = []
    while b < n:
        if b + 2 * m >= n:
            S += [n - b - m]
            m += n - b - m
            b += m
        else:
            if b + 4 * m > n:
                x = (n - b) // 2 - m
                S += [x]
                m += x
            else:
                S += [m]
                m *= 2
            b += m
        d += 1
#  print(S,b)
    print(d)
    for c in S:
        print(c, end=" ")
    print()


T = R()
for _ in range(T):
    solve()
