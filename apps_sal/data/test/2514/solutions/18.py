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
A = [int(i) for i in input().split()]
q = int(input())
B = [[int(i) for i in input().split()] for j in range(q)]
tmp = 0
res = [sum(A)]
tmp = Counter(A)
for i in range(q):
    if B[i][0] in list(tmp.keys()):
        res.append((B[i][1] - B[i][0]) * tmp[B[i][0]])
        if B[i][1] in list(tmp.keys()):
            tmp[B[i][1]] += tmp[B[i][0]]
        else:
            tmp[B[i][1]] = tmp[B[i][0]]
        tmp[B[i][0]] = 0
    else:
        res.append(0)
res = '\n'.join([str(r) for r in list(accumulate(res))[1:]])
print(res)
