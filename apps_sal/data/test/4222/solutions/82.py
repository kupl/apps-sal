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
d = []
A = []
for i in range(k):
    d.append(int(input()))
    A.append([int(i) for i in input().split()])

tmp = [True for i in range(n + 1)]
res = 0

for i in range(k):
    for j in range(d[i]):
        tmp[A[i][j]] = False
for i in range(1, n + 1):
    if tmp[i]:
        res += 1

print(res)
