from heapq import heappush, heappop
(h, w) = map(int, input().split())
s = []
for _ in range(h):
    s_i = list(str(input()))
    s.append(s_i)


def connect(v):
    con_v = []
    if v[0] > 0:
        if s[v[0] - 1][v[1]] == '.':
            con_v.append((v[0] - 1, v[1]))
    if v[1] > 0:
        if s[v[0]][v[1] - 1] == '.':
            con_v.append((v[0], v[1] - 1))
    if v[0] < h - 1:
        if s[v[0] + 1][v[1]] == '.':
            con_v.append((v[0] + 1, v[1]))
    if v[1] < w - 1:
        if s[v[0]][v[1] + 1] == '.':
            con_v.append((v[0], v[1] + 1))
    return con_v


INF = 10 ** 10
VISITED = 1
NOT_VISITED = 0


def longest_bfs(i, j):
    cost = [INF for _ in range(h * w)]
    cost[i * w + j] = 0
    visit = [NOT_VISITED for _ in range(h * w)]
    queue = [(0, (i, j))]
    while len(queue) > 0:
        (c, v) = heappop(queue)
        visit[v[0] * w + v[1]] = VISITED
        for u in connect(v):
            if visit[u[0] * w + u[1]] == VISITED:
                continue
            if cost[u[0] * w + u[1]] > cost[v[0] * w + v[1]] + 1:
                cost[u[0] * w + u[1]] = cost[v[0] * w + v[1]] + 1
                heappush(queue, (cost[u[0] * w + u[1]], u))
    return cost


longest_path = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            continue
        path_length = longest_bfs(i, j)
        for p in path_length:
            if p < INF and p > longest_path:
                longest_path = p
print(longest_path)
