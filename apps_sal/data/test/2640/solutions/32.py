# learnt about numpy from this code thank you nohtaray
# source: https://atcoder.jp/contests/abc129/submissions/5850116
import bisect
import os
from collections import Counter, deque
from fractions import gcd
from functools import lru_cache
from functools import reduce
import functools
import heapq
import itertools
import math
import numpy as np
import re
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

H, W = list(map(int, sys.stdin.readline().split()))

S = np.array([list(sys.stdin.readline().rstrip()) for _ in range(H)]) == '.'
ups = np.zeros((H, W), dtype=int)
downs = np.zeros((H, W), dtype=int)
rights = np.zeros((H, W), dtype=int)
lefts = np.zeros((H, W), dtype=int)

for h in range(1, H):
    ups[h] = (ups[h - 1] + 1) * S[h - 1]
for h in reversed(list(range(H - 1))):
    downs[h] = (downs[h + 1] + 1) * S[h + 1]
for w in range(1, W):
    lefts[:, w] = (lefts[:, w - 1] + 1) * S[:, w - 1]
for w in reversed(list(range(W - 1))):
    rights[:, w] = (rights[:, w + 1] + 1) * S[:, w + 1]
print((((ups + downs + lefts + rights) * S).max() + 1))
