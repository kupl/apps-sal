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
n = int(input())
C = input()
tmp = 0
res = inf
lr = 0
lw = 0
r = C.count('R')
w = C.count('W')
if r == 0 or w == 0:
    res = 0
else:
    for i in range(n):
        tmp = max(lw, r - lr)
        res = min(res, tmp)
        if C[i] == 'R':
            lr += 1
        else:
            lw += 1
print(res)
