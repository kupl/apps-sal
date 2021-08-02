import heapq
n, m = map(int, input().split())
adj_list = [[] for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj_list[a].append((b, c))
    adj_list[b].append((a, c))

# dijkstra


def dijkstra(start):
    prev_node = [-1] * (n + 1)
    INF = 10 ** 10
    VISITED = 1
    NOT_VISITED = 0
    cost = [INF] * (n + 1)
    cost[start] = 0
    visit = [NOT_VISITED] * (n + 1)
    queue = [(cost[start], start)]
    while len(queue) > 0:
        c, v = heapq.heappop(queue)
        visit[v] = VISITED
        for u, cost_vu in adj_list[v]:
            if visit[u] == VISITED:
                continue
            if cost[u] > cost[v] + cost_vu:
                cost[u] = cost[v] + cost_vu
                heapq.heappush(queue, (cost[u], u))
                prev_node[u] = v
    return prev_node


used_edge = [[False] * (n + 1) for i in range(n + 1)]

used_count = 0
for s in range(1, n + 1):
    prev_node = dijkstra(s)
    for i in range(1, n + 1):
        j = prev_node[i]
        if j == -1:
            continue
        if used_edge[i][j] == False:
            used_count += 1
            used_edge[i][j] = True
            used_edge[j][i] = True

print(m - used_count)
