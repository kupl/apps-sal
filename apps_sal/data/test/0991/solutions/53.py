import heapq
(n, m, s) = list(map(int, input().split()))
limit = 2500
s = min(s, limit)
path = [[] for _ in range(n + 1)]
coin = [(0, 0)]
time = [[float('inf') for _ in range(limit + 1)] for _ in range(n + 1)]
queue = []
for i in range(m):
    (u, v, a, b) = list(map(int, input().split()))
    path[u].append((v, a, b))
    path[v].append((u, a, b))
for i in range(n):
    (c, d) = list(map(int, input().split()))
    coin.append((c, d))
time[1][s] = 0
heapq.heappush(queue, (0, 1, s))
while len(queue) != 0:
    (t, v, c) = heapq.heappop(queue)
    for (nv, na, nb) in path[v]:
        if na > c:
            continue
        elif time[nv][c - na] <= t + nb:
            continue
        else:
            time[nv][c - na] = t + nb
            heapq.heappush(queue, (t + nb, nv, c - na))
    nc = min(c + coin[v][0], limit)
    nt = t + coin[v][1]
    if time[v][nc] <= nt:
        continue
    else:
        time[v][nc] = nt
        heapq.heappush(queue, (nt, v, nc))
for i in range(2, n + 1):
    print(min(time[i]))
