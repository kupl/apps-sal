import sys
from functools import lru_cache
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())
T = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    T[a].append(b)
    T[b].append(a)

V = [0] * (N + 1)
for q in range(Q):
    p, x = map(int, input().split())
    V[p] += x


@lru_cache(maxsize=None)
def dfs(i, parent, acc):
    V[i] += acc
    for j in T[i]:
        if j != parent:
            dfs(j, i, V[i])


cur, parent, acc = 1, 0, 0
dfs(cur, parent, acc)
print(*V[1:])
