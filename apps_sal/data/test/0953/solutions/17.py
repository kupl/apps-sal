n = int(input())
p = list(map(int, input().split()))
g = [list() for i in range(n)]
for k in range(n):
    a = list(map(int, input()))
    for i in range(n):
        if a[i]:
            g[k].append(i)


def dfs(v):
    nonlocal c
    was[v] = True
    c[v] = color
    for u in g[v]:
        if not was[u]:
            dfs(u)


c = [0] * n
color = 1
for i in range(n):
    was = [False] * n
    if c[i] == 0:
        dfs(i)
        color += 1
b = [list() for i in range(n)]
for i in range(n):
    b[c[i] - 1].append(p[i])
for i in range(n):
    b[i].sort()
ans = [0] * n
cur = [0] * n
for i in range(n):
    x = c[i] - 1
    ans[i] = b[x][cur[x]]
    cur[x] += 1
print(*ans)
