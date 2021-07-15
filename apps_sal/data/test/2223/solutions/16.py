from sys import stdin
inp = stdin.readline
n, ans = int(inp()), 0
if n & 1:
    print(-1)
    return
g = {i: [set(), 0] for i in range(1, n + 1)}
visited = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, inp().split())
    g[a][0].add(b)
    g[b][0].add(a)
visited = [0, 1] + [0] * (n - 1)
q = [1]
p = [0] * (n + 1)
while q:
    v = q.pop()
    if v != 1 and len(g[v][0]) == 1:
        g[p[v]][0].remove(v)
        g[p[v]][1] += g[v][1] + 1
        q.append(p[v])
        if g[v][1] & 1: ans += 1
        continue
    for i in g[v][0]:
        if not visited[i]:
            visited[i] = True
            p[i] = v
            q.append(i)
            if min(g[v][1], g[i][1]) & 1:
                ans += 1
print(ans)
