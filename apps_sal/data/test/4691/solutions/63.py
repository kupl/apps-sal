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
S = [input() for j in range(n)] # nは行数

tmp = 0
res = 0

tmp = Counter(S)
res = f"""AC x {tmp["AC"]}
WA x {tmp["WA"]}
TLE x {tmp["TLE"]}
RE x {tmp["RE"]}"""

print(res)

