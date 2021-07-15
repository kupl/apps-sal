import sys
import heapq, math
from itertools import zip_longest, permutations, combinations, combinations_with_replacement
from itertools import accumulate, dropwhile, takewhile, groupby
from functools import lru_cache
from copy import deepcopy

N, M, R = list(map(int, input().split()))

RS = list(map(int, input().split()))

G = [[] for _ in range(N + 1)]

for i in range(M):
    A, B, C = list(map(int, input().split()))
    G[A].append((B, C))
    G[B].append((A, C))


def dijkstra(s):
    d = [1 << 28] * (N + 1)
    d[s] = 0
    q = []
    heapq.heappush(q, (0, s))

    while q:
        cur = heapq.heappop(q)

        if d[cur[1]] != cur[0]:
            continue

        for nx in G[cur[1]]:
            if d[nx[0]] > cur[0] + nx[1]:
                d[nx[0]] = cur[0] + nx[1]
                heapq.heappush(q, (cur[0] + nx[1], nx[0]))

    return d


DIRS = [dijkstra(s) for s in RS]
MAT = [[d[r] for r in RS] for d in DIRS]

mem = {}


def solve(idx, st):
    if st == (1 << R) - 1:
        return 0
    if (idx, st) in mem:
        return mem[(idx, st)]

    ret = 1 << 28
    for i in range(R):
        if ((st >> i) & 1) == 0:
            ret = min(ret, solve(i, st | (1 << i)) + MAT[idx][i])

    mem[(idx, st)] = ret
    return ret


print((min([solve(i, 1 << i) for i in range(R)])))

