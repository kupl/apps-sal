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
d = collections.Counter(A)
ct = {}
for k, v in list(d.items()):
    ct[k] = max(0, v * (v - 1) // 2)
sum_ = sum(ct.values())
for ai in A:
    print((sum_ - ct[ai] + max((d[ai] - 1) * (d[ai] - 2) // 2, 0)))
