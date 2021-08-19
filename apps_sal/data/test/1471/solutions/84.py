from collections import deque
N = int(input())
length = {}
conn = [[] for _ in range(N + 1)]
for i in range(N - 1):
    (u, v, w) = [int(x) for x in input().split()]
    conn[u].append(v)
    conn[v].append(u)
    length[u, v] = w
q = deque([1])
dist = [-1] * (N + 1)
dist[1] = 0
while q:
    u = q.popleft()
    for v in conn[u]:
        if dist[v] == -1:
            if u < v:
                dist[v] = dist[u] + length[u, v]
            else:
                dist[v] = dist[u] + length[v, u]
            q.append(v)
for i in range(1, N + 1):
    print(dist[i] % 2)
