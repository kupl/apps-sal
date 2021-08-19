import bisect
import heapq
import itertools
import math
import os
import re
import string
import sys
from collections import Counter, deque, defaultdict
from decimal import Decimal
from fractions import gcd
from functools import lru_cache, reduce
from operator import itemgetter

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

N, K = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))


def bisect_left_callable(fn, x, lo, hi):
    """
    (memo) いっぱい呼ぶなら np.searchsorted のほうがベクトル化されててはやそう
    lo から hi-1 のうち、fn の結果が x 以上となる、最も左の値
    bisect.bisect_left と同じ
    https://docs.python.org/ja/3/library/bisect.html
    :param callable fn:
    :param x:
    :param int lo: 最小値
    :param int hi: 最大値 + 1
    :return: lo <= ret <= hi
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if fn(mid) < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def is_necessary(ai):
    # A[ai] が必要かどうか
    # A[ai] を使わずに K-A[ai] 以上 K 未満を作れるか

    # dp[j]: j を作れる
    dp = np.zeros(K, dtype=bool)
    dp[0] = 1
    for i, a in enumerate(A):
        if i == ai:
            continue
        dp[a:] = dp[a:] | dp[:-a]
    return any(dp[K - A[ai]:])


A.sort()
unnecessary = bisect_left_callable(is_necessary, 1, lo=0, hi=N)
print(unnecessary)
