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

a, b, c, k = [int(i) for i in input().split()]

tmp = 0
res = 0

if k <= a:
    res = k
elif k <= a + b:
    res = a
else:
    res = 2 * a + b - k

print(res)
