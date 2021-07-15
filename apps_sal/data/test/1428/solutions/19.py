import sys
import heapq, math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy

N, C = map(int, input().split())
CM = [list(map(int, input().split())) for _ in range(C)]
NM = [list(map(int, input().split())) for _ in range(N)]

cnt = [[0] * (C + 1) for _ in range(3)]

for i in range(N):
    for j in range(N):
        cnt[(i + j + 2) % 3][NM[i][j]] += 1

ans = 1 << 28
for i in range(1, C + 1):
    for j in range(1, C + 1):
        for k in range(1, C + 1):
            if i == j or j == k or i == k:
                continue
            c = 0
            for l in range(1, C + 1):
                c += cnt[0][l] * CM[l - 1][i - 1]
                c += cnt[1][l] * CM[l - 1][j - 1]
                c += cnt[2][l] * CM[l - 1][k - 1]
            ans = min(ans, c)

print(ans)
