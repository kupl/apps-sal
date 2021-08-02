import heapq


def dijkstra(s):
    dist[s] = 0
    que = []
    heapq.heappush(que, (0, s))
    while len(que) != 0:
        p = heapq.heappop(que)
        v = p[1]
        if (dist[v] < p[0]):
            continue
        for e in graph[v]:
            if dist[e[0]] > dist[v] + e[1]:
                dist[e[0]] = dist[v] + e[1]
                prev[e[0]] = v
                heapq.heappush(que, (dist[e[0]], e[0]))


def get_path(t):
    path = []
    while t != -1:
        path.append(t)
        t = prev[t]
    path = path[::-1]
    return path


N, W = list(map(int, input().split()))
graph = [[] for i in range(N)]
edges = {}
for i in range(W):
    x, y, z = list(map(int, input().split()))
    x -= 1
    y -= 1
    graph[x].append((y, z))
    graph[y].append((x, z))
    edges[(x, y)] = True

for st in range(N):
    dist = [float("inf")] * N
    prev = [-1] * N
    dijkstra(st)
    for i in range(N):
        gp = get_path(i)
        for i in range(1, len(gp)):
            edges[(gp[i - 1], gp[i])] = False

print((sum(edges.values())))
