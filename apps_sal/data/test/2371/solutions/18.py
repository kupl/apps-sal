import sys
import heapq
import math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy
(N, Z, W) = list(map(int, input().split()))
A = list(map(int, input().split()))
if N == 1:
    print(abs(A[-1] - W))
else:
    print(max(abs(A[-1] - W), abs(A[-1] - A[-2])))
