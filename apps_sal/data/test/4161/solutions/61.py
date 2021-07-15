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

k = int(input())

tmp = [[0 for i in range(k + 1)] for j in range(k + 1)]
res = 0

for i in range(1, k + 1):
    for j in range(1, k + 1):
        tmp[i][j] = gcd(i, j)

for a in range(1, k + 1):
    for b in range(k + 1):
        for c in range(k + 1):
            res += tmp[tmp[a][b]][c]

print(res)

