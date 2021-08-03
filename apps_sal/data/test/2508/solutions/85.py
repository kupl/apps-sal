from collections import deque
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

H, W, K = map(int, readline().split())
x1, y1, x2, y2 = map(int, readline().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1
C = read().split()

dist = [[-1] * W for i in range(H)]
dist[x1][y1] = 0
d = deque([[x1, y1]])
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
while d:
    x, y = d.popleft()
    if (x, y) == (x2, y2):
        print(dist[x][y])
        return
    for dx, dy in dxy:
        xx = x
        yy = y
        for i in range(K):
            xx += dx
            yy += dy
            if 0 <= xx < H and 0 <= yy < W and C[xx][yy] != '@':
                if 0 <= dist[xx][yy] <= dist[x][y]:
                    break
                if dist[xx][yy] == -1:
                    d.append([xx, yy])
                dist[xx][yy] = dist[x][y] + 1
            else:
                break

print(-1)
