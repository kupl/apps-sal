import sys
from collections import deque, defaultdict, Counter
from itertools import accumulate, product, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
from math import ceil, floor, sqrt, gcd, inf, log10
from copy import deepcopy
import numpy as np
import scipy as sp
INF = inf
MOD = 1000000007
k = int(input())
tmp = deque(list(range(1, 10)))
res = 0
for i in range(k - 1):
    x = tmp.popleft()
    if x % 10 == 0:
        tmp.append(10 * x + x % 10)
        tmp.append(10 * x + x % 10 + 1)
    elif x % 10 == 9:
        tmp.append(10 * x + x % 10 - 1)
        tmp.append(10 * x + x % 10)
    else:
        tmp.append(10 * x + x % 10 - 1)
        tmp.append(10 * x + x % 10)
        tmp.append(10 * x + x % 10 + 1)
res = tmp.popleft()
print(res)
