import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(lambda x : int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)

mod = 10**9+7
fact = [1] * N
fact_inv = [1] * N
inv = lambda x : pow(x, mod-2, mod)
for i in range(1, N):
    fact[i] = i * fact[i-1] % mod
    fact_inv[i] = inv(fact[i])
comb = lambda n, k : fact[n] * fact_inv[k] * fact_inv[n-k] % mod

value = [1] * N
count = [0] * N
def dfs(par, v):
    for u in G[v]:
        if par == u:
            continue
        dfs(v, u)
        count[v] += count[u]
        value[v] = value[v] * value[u] * comb(count[v], count[u]) % mod
    count[v] += 1

ans = [0] * N
def reroot(par, val_par, cnt_par, v):
    ans[v] = val_par * value[v] * comb(N-1, cnt_par) % mod
    for u in G[v]:
        if par == u:
            continue
        val = ans[v] * inv(value[u] * comb(N-1, count[u])) % mod
        reroot(v, val, N-count[u],  u)

dfs(-1, 0)
reroot(-1, 1, 0, 0)
print(*ans, sep='\n')
