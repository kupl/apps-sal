from decimal import ROUND_HALF_UP, Decimal
from fractions import Fraction as frac
from itertools import combinations as com, permutations as per
from bisect import bisect_left as bileft, bisect_right as biright, insort
from functools import lru_cache
import sys
try:
    import os
    f = open('input.txt', 'r')
    sys.stdin = f
except FileNotFoundError:
    None
from math import sqrt, ceil, floor
from collections import deque, Counter, defaultdict


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(11451419)
(n, k) = list(map(int, input().split()))
ans = 0


def num(j):
    if 2 > j:
        return 0
    if j > 2 * n:
        return 0
    if j < n + 1:
        return j - 1
    sa = 2 * (j - n - 1)
    return j - 1 - sa


for i in range(2, 2 * n - k + 1):
    a = num(i + k)
    b = num(i)
    ans += a * b
print(ans)
