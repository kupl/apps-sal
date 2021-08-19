import sys
import heapq
import math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy
K = int(input())
if K < 10 ** 15:
    (a, b) = (K // 2 + 1, K // 2 + 1)
    if K % 2 == 1:
        a += 2
        b -= 1
    print(2)
    print(a, b)
else:
    N = 50
    A = [i for i in range(50)]
    A = list(map(lambda x: x + K // 50, A))
    r = K % 50
    for i in range(50):
        if i < r:
            A[i] += N
            A[i] -= r - 1
        else:
            A[i] -= r
    print(N)
    print(*A)
