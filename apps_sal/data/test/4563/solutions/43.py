import sys
import heapq
import math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy
N = int(input())
(A, B) = (1, 1)
for i in range(N):
    (XA, XB) = map(int, input().split())
    if A * XB > XA * B:
        d = (A + XA - 1) // XA
        (A, B) = (d * XA, d * XB)
    else:
        d = (B + XB - 1) // XB
        (A, B) = (d * XA, d * XB)
print(A + B)
