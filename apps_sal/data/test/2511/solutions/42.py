import sys
sys.setrecursionlimit(410000)

mod = 10**9 + 7


def dfs(v, pr, k):
    if len(G[v]) > k:
        return 0

    kc = k - 2
    if pr == -1:
        kc = k - 1

    ret = 1

    for vi in G[v]:
        if vi == pr:
            continue
        ret *= kc
        ret %= mod
        kc -= 1

    for vi in G[v]:
        if vi == pr:
            continue
        ret *= dfs(vi, v, k)
        ret %= mod

    return ret


n, k = map(int, input().split())
G = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

print(dfs(0, -1, k) * k % mod)
