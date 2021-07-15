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
    x, y = map(lambda e: int(e) - 1, input().split())
    g[x] += [y]
    g[y] += [x]
used = [False] * n
r = n
for i in range(n):
    if not used[i]:
        r -= 1
        dfs(i)
print(2 ** r)
