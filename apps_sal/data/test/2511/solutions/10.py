import sys
sys.setrecursionlimit(200000)
mod = 10 ** 9 + 7
(N, K) = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    (a, b) = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def dfs(cur, p, nei):
    res = K - nei
    nxnei = min(nei + 1, 2)
    for nx in edges[cur]:
        if nx != p:
            res = res * dfs(nx, cur, nxnei) % mod
            nxnei += 1
    return res


print(dfs(1, 0, 0))
