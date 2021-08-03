import sys
import heapq
import math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy

H, W, D = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]

l = []

for h in range(H):
    for w in range(W):
        l.append((A[h][w], w, h))

l.sort()

S = [0] * (H * W + D + 10)

for i, x, y in l:
    if i + D <= H * W:
        _, xx, yy = l[i + D - 1]
        S[i + D] = abs(xx - x) + abs(yy - y) + S[i]

Q = int(input())

for i in range(Q):
    L, R = list(map(int, input().split()))
    print((S[R] - S[L]))
