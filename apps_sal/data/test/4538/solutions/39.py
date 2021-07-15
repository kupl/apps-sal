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

n, d = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()]for j in range(n)]    # nは行数

tmp = 0
res = 0

for i in range(n):
    x, y = A[i]
    if x ** 2 + y ** 2 <= d ** 2:
        res += 1

print(res)

