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
L = [int(i) for i in input().split()]
tmp = 0
res = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if L[i] != L[j] and L[j] != L[k] and (L[k] != L[i]) and (abs(L[i] - L[j]) < L[k] < L[i] + L[j]):
                res += 1
print(res)
