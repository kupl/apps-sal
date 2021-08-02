import sys
from collections import deque, defaultdict, Counter
from itertools import accumulate, product, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
from math import ceil, floor, sqrt, gcd, inf, pi, cos
from copy import deepcopy
import numpy as np
import scipy as sp

INF = inf
MOD = 1000000007

a, b, h, m = [int(i) for i in input().split()]

tmp = 0
res = 0

theta = 2 * pi * (h / 12.0 + m / 720.0 - m / 60.0)
res = sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(theta))

print(res)
