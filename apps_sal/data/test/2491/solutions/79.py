import sys
INF = 10**30
sys.setrecursionlimit(10**6)


def bellman_ford(s, t, g):
    d = [INF for _ in range(n)]
    d[s] = 0
    val_at_t = INF
    for i in range(n):
        for x, y, z in g:
            if d[y] > d[x] + z:
                d[y] = d[x] + z
        if i == n - 1 and val_at_t > d[t]:
            return []
        val_at_t = d[t]
    return d


n, m = list(map(int, input().split()))
g = []
for _ in range(m):
    x, y, z = list(map(int, input().split()))
    x -= 1
    y -= 1
    z *= -1
    g.append([x, y, z])

ans = bellman_ford(0, n - 1, g)
print((-ans[n - 1] if ans else "inf"))
