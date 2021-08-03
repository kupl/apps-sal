from heapq import *
N, M, S = map(int, input().split())
graph = [[] for _ in range(N)]
amax = 0
for i in range(M):
    u, v, a, b = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append([v, a, b])
    graph[v].append([u, a, b])
    amax = max(amax, a)

lcoins = amax * (N - 1)

cost = list()
time = list()
for _ in range(N):
    c, d = map(int, input().split())
    cost.append(c)
    time.append(d)

INF = float('INF')
M = 2500
if(S >= M):
    S = M - 1

dist = [[INF] * M for _ in range(N)]
dist[0][S] = 0
q = [(0, S, 0)]

while q:
    dv, num, v = heappop(q)

    if dist[v][num] < dv:
        continue

    if num + cost[v] < M and dv + time[v] < dist[v][num + cost[v]]:
        dist[v][num + cost[v]] = dv + time[v]
        heappush(q, (dv + time[v], num + cost[v], v))

    for next, a, b in graph[v]:
        if num >= a and dv + b < dist[next][num - a]:
            dist[next][num - a] = dv + b
            heappush(q, (dv + b, num - a, next))

for i in range(1, N):
    print(min(dist[i]))
