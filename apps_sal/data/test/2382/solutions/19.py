import bisect
import heapq
import itertools
import math
import operator
import os
import re
import string
import sys
from collections import Counter, deque, defaultdict
from copy import deepcopy
from decimal import Decimal
from fractions import gcd
from functools import lru_cache, reduce
from operator import itemgetter, mul, add, xor

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

# 解説AC
N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))


def solve():
    counts = Counter(S)
    nums = list(sorted(list(counts.keys()), reverse=True))
    if counts[nums[0]] > 1:
        return False

    # 木の深さをもって深いやつから使っていく
    trees = [-i for i in range(1, N + 1)]
    heapq.heapify(trees)

    for n in nums[1:]:
        cnt = counts[n]
        if cnt > len(trees):
            return False
        uses = []
        for _ in range(cnt):
            t = -heapq.heappop(trees)
            uses.append(t)
        # 使ったら t-1 個の木に分解する
        for t in uses:
            for i in range(1, t):
                heapq.heappush(trees, -i)
    return True


if solve():
    print('Yes')
else:
    print('No')
