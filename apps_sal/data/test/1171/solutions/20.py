import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce, lru_cache
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
#mod = 998244353
#from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N, K = MAP()
V = LIST()

ans = 0
tmp_sum = 0

for i in range(1, min(K, N) + 1):
    left = K - i
    for j in range(i + 1):
        tmp = V[:j] + V[N - (i - j):]
        tmp.sort()
        idx = bisect_left(tmp, 0)
        ans = max(ans, sum(tmp) - sum(tmp[:min(idx, left)]))

print(ans)
