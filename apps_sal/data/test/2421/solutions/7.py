import heapq


def dijkstra(g: list, start, goal=None):
    num = len(g)
    dist = [float('inf') for i in range(num)]
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        (prov_cost, src) = heapq.heappop(q)
        if dist[src] < prov_cost:
            continue
        for (node, cost) in g[src]:
            if dist[node] > dist[src] + cost:
                dist[node] = dist[src] + cost
                heapq.heappush(q, (dist[node], node))
    return dist


dxdy = ((1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1), (1, 0))
INF = 3 * 10 ** 18
t = int(input())
for _ in range(t):
    (x, y) = list(map(int, input().split()))
    c = list(map(int, input().split()))
    g = [[] for _ in range(25)]
    for i in range(5):
        for j in range(5):
            for k in range(6):
                (dx, dy) = dxdy[k]
                if 0 <= i + dx < 5 and 0 <= j + dy < 5:
                    g[i * 5 + j].append(((i + dx) * 5 + j + dy, c[k]))
    dist = dijkstra(g, 12)
    for i in range(6):
        (dx, dy) = dxdy[i]
        c[i] = dist[12 + dx * 5 + dy]
    ans = 0
    if x > 0 and y > 0:
        m = min(x, y)
        ans += m * c[0]
        x -= m
        y -= m
    elif x < 0 and y < 0:
        m = max(x, y)
        ans -= m * c[3]
        x -= m
        y -= m
    if x > 0:
        ans += x * c[5]
    else:
        ans -= x * c[2]
    if y > 0:
        ans += y * c[1]
    else:
        ans -= y * c[4]
    print(ans)
