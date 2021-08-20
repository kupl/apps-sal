from collections import deque
(n, m) = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    (u, v) = map(int, input().split())
    graph[u - 1].append(v - 1)
(s, t) = map(int, input().split())
s -= 1
t -= 1
q = deque([s])
INF = 10 ** 10
dist = [[INF] * 3 for _ in range(n)]
dist[s][0] = 0
while q:
    node = q.popleft()
    for c_node in graph[node]:
        flg = False
        for i in range(3):
            nd = dist[node][i] + 1
            if dist[c_node][nd % 3] > nd:
                dist[c_node][nd % 3] = nd
                flg = True
        if flg:
            q.append(c_node)
if dist[t][0] == INF:
    print(-1)
else:
    print(dist[t][0] // 3)
