def dfs(v, x, y, t, l, pr):
    ans[v] = x, y
    p = [(0, 1, 3), (0, 1, 2), (1, 2, 3), (0, 2, 3)][t]
    g[v] = [u for u in g[v] if u != pr]
    for i in range(min(len(p), len(g[v]))):
        newx = x + nx[p[i]][0] * l
        newy = y + nx[p[i]][1] * l
        dfs(g[v][i], newx, newy, p[i], l // 4, v)

read = lambda: map(int, input().split())
n = int(input())
g = [list() for i in range(n + 1)]
for i in range(n - 1):
    u, v = read()
    g[u].append(v)
    g[v].append(u)
root = 1
for i in range(n + 1):
    if len(g[i]) > 4:
        print('NO')
        return
ans = [0] * (n + 1)
ans[root] = 0, 0
inf = 10 ** 18
l = inf // 4
nx = (1, 0), (0, -1), (-1, 0), (0, 1)
for i in range(len(g[root])):
    dfs(g[root][i], nx[i][0] * l, nx[i][1] * l, i, l // 4, root)
print('YES')
[print(*i) for i in ans[1:]]
