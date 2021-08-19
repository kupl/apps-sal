from collections import deque
N = int(input())
graph = [[] for _ in range(N)]
dist = [-1] * N
for _ in range(N - 1):
    (u, v, w) = map(int, input().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))
q = deque()
dist[0] = 0
q.append(0)
while len(q) != 0:
    v = q.popleft()
    for (next_v, next_w) in graph[v]:
        if dist[next_v] != -1:
            continue
        dist[next_v] = dist[v] + next_w
        q.append(next_v)
for d in dist:
    if d % 2 == 0:
        print(0)
    else:
        print(1)
