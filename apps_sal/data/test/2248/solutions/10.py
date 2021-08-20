def bfs(x, g):
    (n, q) = (len(g), [x])
    dist = [0 if y == x else -1 for y in range(n)]
    i = 0
    while i < len(q):
        v = q[i]
        i += 1
        for to in g[v]:
            if dist[to] < 0:
                dist[to] = dist[v] + 1
                q.append(to)
    return (q[-1], dist[q[-1]])


(n, m) = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    (a, b) = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)
print(bfs(bfs(0, g)[0], g)[1])
