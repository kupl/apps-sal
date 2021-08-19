import sys
(N, K) = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(N - 1)]
sys.setrecursionlimit(10 ** 9)
edge = [[] for _ in range(N)]
for (u, v) in AB:
    edge[u - 1].append(v - 1)
    edge[v - 1].append(u - 1)
MOD = 10 ** 9 + 7
mod = 10 ** 9 + 7
MAX = K + 10
fac = [0] * MAX
finv = [0] * MAX
inv = [0] * MAX


def cominit():
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod


def cmb(n, r):
    if n < 0 or r < 0 or r > n:
        return 0
    if r > n / 2:
        r = n - r
    return fac[n] * (finv[r] * finv[n - r] % mod) % mod


def permu(n, r):
    if n <= 0 or r <= 0 or r > n:
        return 0
    return fac[n] * finv[n - r] % MOD


cominit()
visited = [False] * N
visited[0] = True


def dfs(s, ans):
    M = len(edge[s]) - 1 * (s != 0)
    if M == 0:
        return ans
    if s == 0:
        ans *= permu(K - 1, M)
        ans %= MOD
    else:
        ans *= permu(K - 2, M)
        ans %= MOD
    for nv in edge[s]:
        if visited[nv]:
            continue
        visited[nv] = True
        ans = dfs(nv, ans)
    return ans


print(dfs(0, K) % MOD)
