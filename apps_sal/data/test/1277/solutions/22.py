import heapq
N, u, v = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N - 1)]

graph = [[] for _ in range(N)]
for i, (Ai, Bi) in enumerate(AB):
    graph[Ai - 1].append(Bi - 1)
    graph[Bi - 1].append(Ai - 1)

MY_INF = 10 ** 18

q = [(0, u - 1)]
d_u = [MY_INF] * N
d_u[u - 1] = 0
while len(q) > 0:
    dist, src = heapq.heappop(q)
    for dst in graph[src]:
        dist_tmp = dist + 1
        if d_u[dst] > dist_tmp:
            d_u[dst] = dist_tmp
            heapq.heappush(q, (dist_tmp, dst))

q = [(0, v - 1)]
d_v = [MY_INF] * N
d_v[v - 1] = 0
while len(q) > 0:
    dist, src = heapq.heappop(q)
    for dst in graph[src]:
        dist_tmp = dist + 1
        if d_v[dst] > dist_tmp:
            d_v[dst] = dist_tmp
            heapq.heappush(q, (dist_tmp, dst))


ans = 0
for i in range(N):
    if d_u[i] < d_v[i] and ans < d_v[i] - 1:
        ans = d_v[i] - 1

print(ans)
