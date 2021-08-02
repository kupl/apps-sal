import sys
from collections import deque, defaultdict, Counter
from itertools import accumulate, product, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
from math import ceil, floor, sqrt, gcd, inf
from copy import deepcopy
import numpy as np
import scipy as sp

INF = inf
MOD = 1000000007

n, m = [int(i) for i in input().split()]
H = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()]for j in range(m)]    # nは行数

tmp = [True for i in range(n + 1)]
res = 0

for i in range(m):
    a, b = A[i]
    if H[a - 1] <= H[b - 1]:
        tmp[a] = False
    if H[a - 1] >= H[b - 1]:
        tmp[b] = False
for i in range(1, n + 1):
    if tmp[i]:
        res += 1

print(res)
