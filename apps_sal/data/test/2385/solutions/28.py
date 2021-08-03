import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().rstrip()


MOD = 10**9 + 7

n = int(input())
g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

lim = 10**5 * 2
fact = [1, 1] + [0] * (lim - 1)
fact_inv = [1, 1] + [0] * (lim - 1)
inv = [0, 1] + [0] * (lim - 1)
for i in range(2, lim + 1):
    fact[i] = fact[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
    fact_inv[i] = fact_inv[i - 1] * inv[i] % MOD


def comb(n, m):
    if n < m or n < 0 or m < 0:
        return 0
    return fact[n] * (fact_inv[m] * fact_inv[n - m] % MOD) % MOD


def icomb(n, m):
    if n < m or n < 0 or m < 0:
        return 0
    return fact_inv[n] * (fact[m] * fact[n - m] % MOD) % MOD


dp = [1] * n
size = [0] * n


def dfs(v, pv):
    for nv in g[v]:
        if nv == pv:
            continue
        dfs(nv, v)
        ns = size[nv] + 1
        size[v] += ns
        dp[v] *= dp[nv] * comb(size[v], ns) % MOD
        dp[v] %= MOD


def dfs2(v, pv):
    for nv in g[v]:
        if nv == pv:
            continue
        d, sz = dp[v], size[v]
        d *= pow(dp[nv], MOD - 2, MOD) * icomb(sz, size[nv] + 1) % MOD
        d %= MOD
        sz -= size[nv] + 1

        size[nv] += sz + 1
        dp[nv] *= d * comb(size[nv], sz + 1) % MOD
        dp[nv] %= MOD
        dfs2(nv, v)


dfs(0, -1)
dfs2(0, -1)
print(*dp, sep="\n")
