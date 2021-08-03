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
A = [int(i) for i in input().split()]

tmp = 0
res = "No"

A = sorted(A, reverse=True)
if A[m - 1] * m * 4 >= sum(A):
    res = "Yes"

print(res)
