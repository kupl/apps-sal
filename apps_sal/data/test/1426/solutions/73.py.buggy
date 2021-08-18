from collections import deque
N, M = map(int, input().split())
UV = [tuple(map(int, input().split())) for i in range(M)]
S, T = map(int, input().split())
S -= 1
T -= 1
es = [[] for _ in range(3 * N)]
for u, v in UV:
    u, v = u - 1, v - 1
    es[3 * u].append(3 * v + 1)
    es[3 * u + 1].append(3 * v + 2)
    es[3 * u + 2].append(3 * v)

dist = [0] * (3 * N)
visited = [0] * (3 * N)
visited[3 * S] = 1
q = deque([3 * S])
while q:
    v = q.popleft()
    if v == 3 * T:
        assert dist[v] % 3 == 0
        print(dist[v] // 3)
        return
    for to in es[v]:
        if visited[to]:
            continue
        visited[to] = 1
        dist[to] = dist[v] + 1
        q.append(to)
print(-1)
