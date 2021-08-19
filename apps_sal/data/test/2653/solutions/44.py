import sys
from functools import lru_cache
sys.setrecursionlimit(10 ** 7)
(N, Q) = map(int, input().split())
T = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    (a, b) = map(int, input().split())
    T[a].append(b)
    T[b].append(a)
S = [0] * (N + 1)
for _ in range(Q):
    (p, x) = map(int, input().split())
    S[p] += x


@lru_cache(maxsize=None)
def dfs(now, prev=-1):
    for next in T[now]:
        if next == prev:
            continue
        S[next] += S[now]
        dfs(next, now)


dfs(1)
print(*S[1:])
