def dfs(t):
    nonlocal used, g
    used[t] = True
    for k in g[t]:
        if not used[k]:
            used[k] = True
            dfs(k)


n, m = map(int, input().split())
g = [[] for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    g[x - 1].append(y - 1)
    g[y - 1].append(x - 1)
used = [False] * n
ans = n
for i in range(n):
    if not used[i]:
        ans -= 1
        dfs(i)
print(2**ans)
