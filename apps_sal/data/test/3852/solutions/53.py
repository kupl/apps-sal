import sys
import heapq
import math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy

N = int(input())
A = list(map(int, input().split()))
minv, maxv = min(A), max(A)
mini, maxi = -1, -1

for i in range(N):
    if minv == A[i]:
        mini = i
    if maxv == A[i]:
        maxi = i

if minv * maxv >= 0:
    print((N - 1))
    if minv >= 0:
        for i in range(N - 1):
            print((i + 1, i + 2))
    else:
        for i in range(N, 1, -1):
            print((i, i - 1))
else:
    print((2 * N - 1))
    if abs(minv) < abs(maxv):
        for i in range(N):
            print((maxi + 1, i + 1))
        for i in range(N - 1):
            print((i + 1, i + 2))
    else:
        for i in range(N):
            print((mini + 1, i + 1))
        for i in range(N, 1, -1):
            print((i, i - 1))
