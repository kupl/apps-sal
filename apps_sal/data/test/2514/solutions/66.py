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

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin


def ni(): return int(ns())
def nf(): return float(ns())
def na(): return list(map(int, stdin.readline().split()))
def nb(): return list(map(float, stdin.readline().split()))
def ns(): return stdin.readline().rstrip()


N = ni()
A = na()
Q = ni()
ans = sum(A)
d = collections.Counter(A)
for i in range(Q):
    B, C = na()
    ct_b = d[B]
    if ct_b == 0:
        print(ans)
    else:
        ans += ct_b * (C - B)
        d[C] += ct_b
        d[B] = 0
        print(ans)
