import heapq
(n, m) = map(int, input().split())
vertexs = dict()
for i in range(1, n + 1):
    vertexs[i] = []
for j in range(m):
    (v, u) = map(int, input().split())
    if v != u:
        vertexs[v].append(u)
        vertexs[u].append(v)
vis = dict()
dp = [1]
vis[1] = True
answers = []
for i in range(n):
    next_v = heapq.heappop(dp)
    answers.append(next_v)
    vis[next_v] = True
    for u in vertexs[next_v]:
        if u not in vis:
            heapq.heappush(dp, u)
            vis[u] = True
print(*answers, sep=' ')
