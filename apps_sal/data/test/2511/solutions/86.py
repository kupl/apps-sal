import sys
sys.setrecursionlimit(10**6)
MOD = 10**9 + 7


def facinv(N):
    fac, finv, inv = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)
    fac[0] = 1; fac[1] = 1; finv[0] = 1; finv[1] = 1; inv[1] = 1
    for i in range(2, N + 1):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD
    return fac, finv, inv


def PER(n, r):
    if n < r or r < 0:
        return 0
    else:
        return (fac[n] * finv[n - r])


def dfs(v, p, dep):
    nonlocal res
    c = 0
    for nv in G[v]:
        if nv == p:
            continue
        dfs(nv, v, dep + 1)
        c += 1
    if dep == 0:
        res = (res * PER(K - 1, c) % MOD)
    else:
        res = (res * PER(K - 2, c) % MOD)


N, K = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)
fac, finv, inv = facinv(max(K, N))
res = K
dfs(0, -1, 0)
print(res % MOD)
