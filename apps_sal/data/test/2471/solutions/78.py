import sys
import heapq
import math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy
(H, W, N) = map(int, input().split())
m = {}
for i in range(N):
    (a, b) = map(int, input().split())
    for j in range(-2, 1):
        for k in range(-2, 1):
            if not 1 <= a + j <= H - 2 or not 1 <= b + k <= W - 2:
                continue
            m[a + j, b + k] = m.get((a + j, b + k), 0) + 1
ans = [0] * 10
for (k, v) in m.items():
    ans[v] += 1
ans[0] = (H - 2) * (W - 2) - sum(ans[1:10])
for i in range(10):
    print(ans[i])
