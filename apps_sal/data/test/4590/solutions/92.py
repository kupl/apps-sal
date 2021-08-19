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


(N, M, K) = na()
A = na()
B = na()
now = 0
ct = 0
x = -1
y = 0
ans = 0
for i in range(N):
    if A[i] + now <= K:
        now += A[i]
        ct += 1
        x += 1
    else:
        break
res = K - now
ans = ct
while y < M:
    if res - B[y] >= 0:
        ct += 1
        ans = max(ct, ans)
        res -= B[y]
        y += 1
    elif res - B[y] < 0 and x >= 0:
        res += A[x]
        ct -= 1
        x -= 1
    else:
        break
print(ans)
