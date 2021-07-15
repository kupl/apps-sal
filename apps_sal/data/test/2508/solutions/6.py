from collections import deque

H, W, K = list(map(int, input().split()))
sx, sy, tx, ty = [int(a) - 1 for a in input().split()]
INF = 10**18

A = [input() for _ in range(H)]

minDist = [[INF] * W for _ in range(H)]
minDist[sx][sy] = 0
que = deque([(0, sx, sy)])

while que:
    dist, nx, ny = que.popleft()
    if nx == tx and ny == ty:
        break

    for i in range(1, K + 1):
        if nx + i >= H:
            break
        if minDist[nx + i][ny] <= dist or A[nx + i][ny] == '@':
            break
        if minDist[nx + i][ny] > dist + 1:
            minDist[nx + i][ny] = dist + 1
            que.append((dist + 1, nx + i, ny))
    for i in range(1, K + 1):
        if nx - i < 0:
            break
        if minDist[nx - i][ny] <= dist or A[nx - i][ny] == '@':
            break
        if minDist[nx - i][ny] > dist + 1:
            minDist[nx - i][ny] = dist + 1
            que.append((dist + 1, nx - i, ny))
    for i in range(1, K + 1):
        if ny + i >= W:
            break
        if minDist[nx][ny + i] <= dist or A[nx][ny + i] == '@':
            break
        if minDist[nx][ny + i] > dist + 1:
            minDist[nx][ny + i] = dist + 1
            que.append((dist + 1, nx, ny + i))
    for i in range(1, K + 1):
        if ny - i < 0:
            break
        if minDist[nx][ny - i] <= dist or A[nx][ny - i] == '@':
            break
        if minDist[nx][ny - i] > dist + 1:
            minDist[nx][ny - i] = dist + 1
            que.append((dist + 1, nx, ny - i))

ans = minDist[tx][ty]
print((ans if ans < INF else -1))

