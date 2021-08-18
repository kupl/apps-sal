def dijkstra(s):
    import heapq
    dist = [inf for i in range(n)]
    dist[s] = 0
    mirai = [True for i in range(n)]
    mirai[s] = False

    queue = []
    for kyori, to in G[s]:
        heapq.heappush(queue, kyori * 10**6 + to)
    while queue:
        minedge = heapq.heappop(queue)
        if not mirai[minedge % (10**6)]:
            continue
        v = minedge % (10**6)
        dist[v] = minedge // (10**6)
        mirai[v] = False
        for kyori, to in G[v]:
            if mirai[to]:
                heapq.heappush(queue, (kyori + dist[v]) * (10**6) + to)
    return dist


n, m = list(map(int, input().split()))
inf = 10**10
G = [[] for i in range(n)]
HEN = []
for i in range(m):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    G[a].append((c, b))
    G[b].append((c, a))
    HEN.append((a, b, c))

MIN = [[10**10] * n for i in range(n)]
for i in range(n):
    MIN[i] = dijkstra(i)
ans = 0
for a, b, c in HEN:
    for s in range(n):
        if MIN[s][a] + c == MIN[s][b]:
            break
        if MIN[s][b] + c == MIN[s][a]:
            break
    else:
        ans += 1
print(ans)
