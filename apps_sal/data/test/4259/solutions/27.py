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
a, b = [int(i) for i in input().split()]

tmp = 0
res = "NG"

for i in range(a, b + 1):
    if i % k == 0:
        res = "OK"

print(res)
