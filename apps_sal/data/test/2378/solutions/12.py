import sys
sys.setrecursionlimit(200200)
mod = 10 ** 9 + 7
(N, *AB) = map(int, open(0).read().split())
E = [[] for _ in range(N + 1)]
for (i, (a, b)) in enumerate(zip(*[iter(AB)] * 2)):
    E[a - 1].append((b - 1, i))
    E[b - 1].append((a - 1, i))
X = [0] * N


def dfs(u, i):
    res = 1
    for (v, c) in E[u]:
        if i != c:
            res += dfs(v, c)
    X[i] = res
    return res


dfs(0, -1)
I = [1] * (N + 1)
inv = pow(2, mod - 2, mod)
for i in range(N):
    I[i + 1] = I[i] * inv % mod
ans = (I[N] + 1) * (N - 1) - inv * N - I[N] + 1
for e in range(N - 1):
    ans -= I[X[e]] + I[N - X[e]]
    ans %= mod
print(ans)
