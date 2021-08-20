from collections import deque
(H, W) = map(int, input().split())
S = [input() for _ in range(H)]
s = 0
for c in S:
    s += c.count('.')
que = deque()
dist = [[-1 for j in range(W)] for i in range(H)]
dist[0][0] = 0
st = (0, 0)
que.append(st)
dydx = [(1, 0), (0, 1), (-1, 0), (0, -1)]
while que:
    (p, q) = que.popleft()
    for (dy, dx) in dydx:
        if 0 <= p + dy and p + dy < H and (0 <= q + dx) and (q + dx < W):
            if dist[p + dy][q + dx] != -1 or S[p + dy][q + dx] != '.':
                continue
            dist[p + dy][q + dx] = dist[p][q] + 1
            que.append((p + dy, q + dx))
if dist[H - 1][W - 1] == -1:
    print(-1)
else:
    print(s - dist[H - 1][W - 1] - 1)
