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

tmp = 0
res = 0

if n % 10 in [2, 4, 5, 7, 9]:
    res = "hon"
elif n % 10 in [0, 1, 6, 8]:
    res = "pon"
else:
    res = "bon"

print(res)
