from sys import setrecursionlimit
setrecursionlimit(2 * 10 ** 5 + 10)

mod = 10 ** 9 + 7

N, *AB = map(int, open(0).read().split())

E = [[] for _ in range(N)]
for i, (a, b) in enumerate(zip(*[iter(AB)] * 2)):
    E[a - 1].append((b - 1, i))
    E[b - 1].append((a - 1, i))

X = [0] * N

def dfs(u, p):
    res = 1
    for v, c in E[u]:
        if p != c:
            res += dfs(v, c)
    X[p] = res
    return res

dfs(0, -1)

I = [1]
inv = pow(2, mod - 2, mod)
for i in range(N):
    I.append(I[-1] * inv % mod)

ans = - inv * N - I[N] + 1 + sum((1 - I[x]) * (1 - I[N - x]) for x in X)

print(ans % mod)
