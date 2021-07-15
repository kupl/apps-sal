from collections import deque

N, Q = list(map(int, input().split())) # Nは頂点の数、Qは操作の回数
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

counts = [0] * (N+1)
for _ in range(Q):
    p, x  = list(map(int, input().split()))
    counts[p] += x
visited = [-1] * (N+1)

q = deque()
q.append(1)
visited[1] = 1
while q:
    node = q.pop()

    next_nodes = graph[node]
    for next in next_nodes:
        if visited[next] != -1:
            continue
        q.append(next)
        visited[next] = 1
        counts[next] += counts[node]

print((*counts[1:]))



