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

s = int(input())

tmp = 0
res = 0

A = [0 for i in range(s + 1)]
for i in range(s + 1):
    if i == 0:
        A[i] = 1
    elif i == 1 or i == 2:
        A[i] = 0
    else:
        A[i] = sum(A[:i - 2]) % MOD
res = A[s]

print(res)

