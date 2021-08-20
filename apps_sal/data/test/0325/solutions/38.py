import sys
from collections import deque


def dfs(x, s):
    used = {s}
    search = deque([s])
    while search:
        ss = search.pop()
        for sss in x[ss]:
            if sss in used:
                continue
            used.add(sss)
            search.append(sss)
    return used


def bellmanford(edges):
    coins = [-float('inf')] * N
    coins[0] = 0
    for _ in range(N):
        f = True
        for (u, v, c) in edges:
            if coins[u] + c > coins[v]:
                coins[v] = coins[u] + c
                f = False
        if f:
            return max(0, coins[-1])
    return -1


(N, M, P) = map(int, input().split())
ABC = []
Adake = [[] for _ in range(N)]
Bdake = [[] for _ in range(N)]
for _ in range(M):
    (A, B, C) = map(int, input().split())
    ABC.append((A - 1, B - 1, C - P))
    Adake[A - 1].append(B - 1)
    Bdake[B - 1].append(A - 1)
U = dfs(Adake, 0) & dfs(Bdake, N - 1)
ABC = [(a, b, c) for (a, b, c) in ABC if a in U and b in U]
print(bellmanford(ABC))
