import heapq

def dijkstra(s):
    inf = 1145141919810
    dist = [inf] * v
    dist[s] = 0
    c = [0] * v
    p = []
    heapq.heapify(p)
    heapq.heappush(p, (dist[s], s))
    while p:
        d, u = heapq.heappop(p)
        if dist[u] < d:
            continue
        c[u] = 1
        for g in G[u]:
            if c[g[0]] == 0 and dist[u] + g[1] < dist[g[0]]:
                dist[g[0]] = dist[u] + g[1]
                heapq.heappush(p, (dist[g[0]], g[0]))
    return dist

n, m = map(int, input().split())
v = n
G = [[] for _ in range(v)]
E = []
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append([b, c])
    G[b].append([a, c])
    E.append([a, b, c])
mindist = [dijkstra(i) for i in range(v)]
ans = m
for e in E:
    for i in range(n):
        if mindist[i][e[0]] - mindist[i][e[1]] == e[2]:
            ans -= 1
            break
print(ans)
