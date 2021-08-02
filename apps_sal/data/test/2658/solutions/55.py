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

n, k = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

tmp = [0 for i in range(n + 1)]
cnt = 0
res = 1

while cnt < k:
    cnt += 1
    if tmp[res] == 0:
        tmp[res] = cnt
    else:
        cnt += (k - cnt) // (cnt - tmp[res]) * (cnt - tmp[res])
        tmp[res] = cnt
    res = A[res - 1]

print(res)
