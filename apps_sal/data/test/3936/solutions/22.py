from functools import lru_cache, reduce
from bisect import bisect_left, bisect_right
import random
import operator
import string
import sys
from collections import deque, defaultdict, namedtuple
import heapq
from math import sqrt, factorial, gcd, ceil, atan, pi
from itertools import permutations


def input():
    return sys.stdin.readline().strip()


MOD = int(1000000000.0) + 7
INF = float('inf')
sys.setrecursionlimit(int(10000000.0))


def solve():
    n = int(input())
    a = input()
    b = input()
    ans = 1
    i = 0
    f = -1
    while i < n:
        if a[i] != b[i]:
            if f == -1:
                ans *= 6
            elif f == 1:
                ans *= 3
            else:
                ans *= 2
            i += 2
            f = 1
        else:
            if f == -1:
                ans *= 3
            elif f == 0:
                ans *= 2
            i += 1
            f = 0
    print(ans % MOD)


T = 1
for case in range(1, T + 1):
    ans = solve()
'\n\na b\nb a\n\na b\nb c\n\na c\nb a\n\n'
