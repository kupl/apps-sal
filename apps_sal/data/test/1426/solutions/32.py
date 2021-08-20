from collections import deque
(n, m) = map(int, input().split())
G = [[] for i in range(n)]
for i in range(m):
    (u, v) = map(int, input().split())
    G[u - 1].append(v - 1)
(s, t) = map(int, input().split())
s -= 1
t -= 1
dist = [[-1] * 3 for i in range(n)]
dist[s][0] = 0
q = deque()
q.append([s, 0])
while q:
    (cur, parity) = q.popleft()
    for nx in G[cur]:
        nx_parity = (parity + 1) % 3
        if dist[nx][nx_parity] == -1:
            dist[nx][nx_parity] = dist[cur][parity] + 1
            q.append([nx, nx_parity])
if dist[t][0] == -1:
    print(-1)
else:
    print(int(dist[t][0] // 3))
