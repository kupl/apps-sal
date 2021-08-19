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
A = [[int(i) for i in input().split()]for j in range(n)]    # nは行数

tmp = 0
res = 0

x = np.median(np.array(A), axis=0)
if n % 2 == 0:
    res = int((x[1] - x[0]) * 2 + 1)
else:
    res = int(x[1] - x[0] + 1)

print(res)
