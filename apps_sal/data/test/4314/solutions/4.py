import sys
import heapq, math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy

H, W = list(map(int, input().split()))

ignore = "".join(["." for _ in range(W)])

A = list([x for x in [input() for _ in range(H)] if x != ignore])
H = len(A)
B = [[] for _ in range(H)]

for w in range(W):
    if list([x for x in A if x[w] == "#"]):
        for i in range(H):
            B[i].append(A[i][w])

for h in range(H):
    print(("".join(B[h])))

