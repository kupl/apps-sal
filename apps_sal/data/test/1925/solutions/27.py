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

a, b, n = [int(i) for i in input().split()]

tmp = 0
res = 0

for x in range(min(b, n), -1, -1):
    res = floor(a * x / b) - a * floor(x / b)
    if res > 0:
        break

print(res)

