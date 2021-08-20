import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import bisect
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
import sys
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
mod = 10 ** 9 + 7
stdin = sys.stdin


def ni():
    return int(ns())


def nf():
    return float(ns())


def na():
    return list(map(int, stdin.readline().split()))


def nb():
    return list(map(float, stdin.readline().split()))


def ns():
    return stdin.readline().rstrip()


def make_divisors(n):
    (lower_divisors, upper_divisors) = ([], [])
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N = ni()
A = na()
d = collections.Counter(A)
dp = [0] * (10 ** 6 + 10)
A.sort()
pre = -1
ans = 0
for ai in A:
    if pre == ai:
        continue
    pre = ai
    if dp[ai] == 0 and d[ai] == 1:
        ans += 1
    for j in range(ai, 10 ** 6 + 1, ai):
        dp[j] = 1
print(ans)
