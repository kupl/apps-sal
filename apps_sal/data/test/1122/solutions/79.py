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

tmp_l = m + 1
tmp_r = m - 1
res = []

while tmp_r > 0:
    res.append([tmp_l + 1, tmp_l + tmp_r + 1])
    tmp_l += 1
    tmp_r -= 2
tmp_l = 0
tmp_r = m
while tmp_r > 0:
    res.append([tmp_l + 1, tmp_l + tmp_r + 1])
    tmp_l += 1
    tmp_r -= 2
res = "\n".join([" ".join([str(i) for i in j]) for j in res])

print(res)

