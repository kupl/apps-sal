import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    (a, b) = map(lambda x: int(x) - 1, input().split())
    G[a].append(b)
    G[b].append(a)
mod = 10 ** 9 + 7
fact = [1] * N
fact_inv = [1] * N
for i in range(1, N):
    fact[i] = i * fact[i - 1] % mod


def inv(x):
    return pow(x, mod - 2, mod)


fact_inv[N - 1] = inv(fact[N - 1])
for i in range(1, N)[::-1]:
    fact_inv[i - 1] = i * fact_inv[i] % mod


def comb(n, k):
    return fact[n] * fact_inv[k] * fact_inv[n - k] % mod


dp = [1] * N
size = [0] * N


def dfs(par, v):
    for u in G[v]:
        if par == u:
            continue
        dfs(v, u)
        size[v] += size[u]
        dp[v] = dp[v] * dp[u] * fact_inv[size[u]] % mod
    dp[v] = dp[v] * fact[size[v]] % mod
    size[v] += 1


ans = [0] * N


def reroot(par, val_par, size_par, v):
    ans[v] = val_par * dp[v] * comb(N - 1, size_par) % mod
    for u in G[v]:
        if par == u:
            continue
        val = ans[v] * inv(dp[u] * comb(N - 1, size[u])) % mod
        reroot(v, val, N - size[u], u)


dfs(-1, 0)
reroot(-1, 1, 0, 0)
print(*ans, sep='\n')
