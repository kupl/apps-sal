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

a, b, c, d = [int(i) for i in input().split()]

tmp = 0
res = "No"

while True:
    c -= b
    if c <= 0:
        res = "Yes"
        break
    a -= d
    if a <= 0:
        break

print(res)

