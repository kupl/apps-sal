from collections import deque
dxdy = ((-1, 0), (1, 0), (0, -1), (0, 1))  # タプルやリストで持っておくと便利

H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
mp = [input() for _ in range(H)]
INF = 10**10
dist = [[INF] * W for _ in range(H)]
dist[x1 - 1][y1 - 1] = 0
q = deque()
q.append((x1 - 1, y1 - 1))  # スタート地点をenqueue
while(q):
    x, y = q.popleft()
    if x == x2 - 1 and y == y2 - 1:
        print(dist[x2 - 1][y2 - 1])
        return
    else:
        for dx, dy in dxdy:
            for i in range(1, K + 1):
                nx = x + dx * i
                ny = y + dy * i
                if not (0 <= nx < H and 0 <= ny < W) or mp[nx][ny] == '@':
                    break
                if dist[nx][ny] <= dist[x][y]:
                    break
                if dist[nx][ny] == INF:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
print(-1)
