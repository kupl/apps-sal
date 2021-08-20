import sys
import heapq
import math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy
N = int(input())
A = [0] + list(map(int, input().split())) + [0]
S = 0
for i in range(N + 1):
    S += abs(A[i] - A[i + 1])
for i in range(N):
    print(S - abs(A[i] - A[i + 1]) - abs(A[i + 1] - A[i + 2]) + abs(A[i] - A[i + 2]))
