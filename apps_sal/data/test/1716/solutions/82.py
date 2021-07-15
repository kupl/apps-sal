import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
import numpy as np
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, M, Q = MAP()
LR = [LIST() for _ in range(M)]
pq = [LIST() for _ in range(Q)]

x = np.zeros((N+1, N+1), dtype=np.int64)
for L, R in LR:
    x[L, R] += 1
x = x.cumsum(axis=0).cumsum(axis=1)

for p, q in pq:
    print((x[q][q]-x[q][p-1]-x[p-1][q]+x[p-1][p-1]))

