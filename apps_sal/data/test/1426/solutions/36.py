from collections import deque
(N, M, *f) = map(int, open(0).read().split())
uv = [f[i:i + 2] for i in range(0, len(f) - 2, 2)]
S = f[-2]
T = f[-1]
connected = [[] for _ in range(N + 1)]
for (u, v) in uv:
    connected[u].append(v)
dist = [[-1] * 3 for _ in range(N + 1)]
dist[S][0] = 0
ans = 0
d = deque([(S, 0)])
while d:
    temp = d.popleft()
    for edge in connected[temp[0]]:
        if edge == T and temp[1] == 2:
            print((dist[temp[0]][2] + 1) // 3)
            break
        elif dist[edge][(temp[1] + 1) % 3] < 0:
            dist[edge][(temp[1] + 1) % 3] = dist[temp[0]][temp[1]] + 1
            d.append((edge, (temp[1] + 1) % 3))
    else:
        continue
    break
else:
    print(-1)
