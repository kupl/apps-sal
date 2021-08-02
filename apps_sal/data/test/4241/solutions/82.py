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

s = input()
t = input()

tmp = 0
res = 0

res = INF
ls = len(s)
lt = len(t)
for i in range(ls - lt + 1):
    tmp = 0
    for j in range(lt):
        if t[j] != s[i + j]:
            tmp += 1
    res = min(res, tmp)

print(res)
