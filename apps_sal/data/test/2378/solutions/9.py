import sys
sys.setrecursionlimit(200200)
input = sys.stdin.readline
MOD = 10**9 + 7
N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N - 1)]
G = [[] for _ in range(N)]
for i, (a, b) in enumerate(AB):
    a -= 1
    b -= 1
    G[a].append((b, i))
    G[b].append((a, i))

P = [0] * N
visited = [False] * N
visited[0] = True


def dfs(x, i):
    e = 1
    for v, c in G[x]:
        if not visited[v]:
            visited[v] = True
            e += dfs(v, c)
    P[i] = e
    return e


dfs(0, -1)
W = [1] * (N + 1)
inv_2 = pow(2, MOD - 2, MOD)
for i in range(N):
    W[i + 1] = W[i] * inv_2 % MOD
ans = (W[N] + 1) * (N - 1) % MOD
for i in range(N - 1):
    ans -= W[P[i]] + W[N - P[i]]
    ans %= MOD
print((ans - inv_2 * N - W[N] + 1) % MOD)
