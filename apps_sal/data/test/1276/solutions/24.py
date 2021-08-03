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
s = input()

tmp = 0
res = s.count("R") * s.count("G") * s.count("B")

for i in range(n - 2):
    for j in range(i + 1, floor((n + i + 1) / 2)):
        k = 2 * j - i
        if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
            res -= 1

print(res)
