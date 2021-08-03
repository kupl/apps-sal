import sys
sys.setrecursionlimit(10**6)

n, u, v = list(map(int, input().split()))
# よりたかはしくんが早く辿り着ける葉のうち、青木君から最も遠いで
u -= 1
v -= 1

g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = [int(x) - 1 for x in input().split()]
    g[a].append(b)
    g[b].append(a)

INF = 1 << 30
t = [INF] * n
a = [INF] * n

t[u] = 0
a[v] = 0


def dfs(v, p, d):
    for nv in g[v]:
        if nv == p:
            continue
        if d[nv] == INF:
            d[nv] = d[v] + 1
            dfs(nv, v, d)


dfs(u, -1, t)
dfs(v, -1, a)

ans = 0
for i in range(n):
    if t[i] < a[i]:
        ans = max(ans, a[i] - 1)
print(ans)
