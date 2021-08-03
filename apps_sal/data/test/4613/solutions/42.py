n, m = map(int, input().split())
s = [set() for i in range(n)]
e = []
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    s[a].add(b)
    s[b].add(a)
    e.append([a, b])


def dfs(u, v, c):
    visited[u] = 1
    c += 1
    if u == v:
        d.append(c)
        return True
    for i in s[u]:
        if visited[i]:
            continue
        if c == 1:
            if i == v:
                continue
        dfs(i, v, c)


cnt = 0
for i in range(m):
    x, y = e[i][0], e[i][1]
    visited = [0 for i in range(n)]
    d = []
    dfs(x, y, 0)
    if len(d) > 0:
        cnt += 1
print(m - cnt)
