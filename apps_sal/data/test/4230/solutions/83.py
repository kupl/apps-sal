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

x, n = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]

tmp = 0
res = 0

P = np.array(P) - x

while True:
    if not -res in P:
        res *= -1
        break
    if not res in P:
        break
    res += 1
res += x

print(res)
