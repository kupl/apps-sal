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

tmp = 0
res = 1

A = sorted(A)
for i in range(n):
    res *= A[i]
    if res > 10 ** 18:
        res = -1
        break
    if res == 0:
        break

print(res)
