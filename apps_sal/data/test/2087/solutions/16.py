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
def input(): return sys.stdin.readline().strip()


sys.setrecursionlimit(11451419)


def f(n):
    return n * (n + 1) // 2


a, b, c = list(map(int, input().split()))
mod = 998244353
print((((f(a) % mod) * (f(b) % mod) * (f(c) % mod)) % mod))
