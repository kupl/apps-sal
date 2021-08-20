from collections import deque
INF = 10 ** 18
(N, M) = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    (a, b) = map(int, input().split())
    graph[a - 1].append(b - 1)
loopsize = INF
for root in range(N):
    queue = deque([root])
    dist = [INF for _ in range(N)]
    dist[root] = 0
    prev = [None for _ in range(N)]
    while queue:
        node = queue.popleft()
        for adj in graph[node]:
            if adj == root:
                dist[root] = dist[node] + 1
                prev[root] = node
                break
            if dist[adj] != INF:
                continue
            dist[adj] = dist[node] + 1
            prev[adj] = node
            queue.append(adj)
        else:
            continue
        break
    else:
        continue
    if loopsize > dist[root]:
        loopsize = dist[root]
        path = [root]
        node = root
        while prev[node] != root:
            node = prev[node]
            path.append(node)
if loopsize != INF:
    print(loopsize)
    for node in path:
        print(node + 1)
else:
    print(-1)
