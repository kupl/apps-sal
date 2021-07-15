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

def base_n(n, base):
    if (n - 1) // base:
        return base_n((n - 1) // base, base) + [(n - 1) % base + 1]
    return [(n - 1) % base + 1]

INF = inf
MOD = 1000000007

n = int(input())

tmp = n
res = 0

res = "".join([chr(i + 96) for i in base_n(n, 26)])

print(res)

