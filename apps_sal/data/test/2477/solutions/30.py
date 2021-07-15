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

tmp = 0
res = inf
low = 0
high = max(A)
while low <= high:
    mid = (low + high) // 2
    tmp = 0
    for i in range(n):
        if mid > 0:
            tmp += ceil(A[i] / mid) - 1
        else:
            tmp = inf
    if tmp <= k:
        res = min(res, mid)
        high = mid - 1
    else:
        low = mid + 1

print(res)

