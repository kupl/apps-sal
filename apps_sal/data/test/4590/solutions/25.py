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

n, m, k = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

tmp = sum(A)
cnt = len(A)
res = 0

A = deque(A)
B = deque(B)

while True:
    if tmp <= k:
        res = max(res, cnt)
        if len(B) <= 0:
            break
        b = B.popleft()
        tmp += b
        cnt += 1
    else:
        if len(A) <= 0:
            break
        a = A.pop()
        tmp -= a
        cnt -= 1

print(res)
