import sys
import heapq, math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy

N, X, M = map(int, input().split())

A = [X]
B = [0, X]
S = set(A)

while not A[-1] * A[-1] % M in S:
    V = A[-1] * A[-1] % M
    B.append(B[-1] + V)
    A.append(V)
    S.add(V)

idx = A.index(A[-1] * A[-1] % M)

ans = 0

if idx < N:
    l = len(A) - idx
    ans += B[idx]
    N -= idx

    ans += (B[-1] - B[idx]) * (N // l)
    ans += B[idx + N % l] - B[idx]

    print(ans)
else:
    print(B[N])
