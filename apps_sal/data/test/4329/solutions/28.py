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
s = input()
t = input()
tmp = 0
res = 'No'
if s == t[:-1]:
    res = 'Yes'
print(res)
