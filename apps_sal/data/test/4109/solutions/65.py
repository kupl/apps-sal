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

n, m, x = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()]for j in range(n)]    # nは行数

tmp = 0
res = inf

for i in range(2 ** n):
    s = f"{i:0{n}b}"
    tmp = [0 for i in range(m + 1)]
    for j in range(n):
        if s[j] == "1":
            for k in range(m + 1):
                tmp[k] += A[j][k]
    flg = True
    for k in range(1, m + 1):
        if tmp[k] < x:
            flg = False
    if flg:
        res = min(res, tmp[0])
if res == inf:
    res = -1

print(res)
