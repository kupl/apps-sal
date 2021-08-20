from collections import deque
import sys


def bfs(M, sy, sx, gy, gx):
    queue = deque([[sy, sx]])
    M[sy][sx] = 0
    while queue:
        (y, x) = queue.popleft()
        if [y, x] == [gy, gx]:
            return M[y][x]
        for (dx, dy) in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            for k in range(1, K + 1):
                new_x = x + dx * k
                new_y = y + dy * k
                if 0 <= new_y < H and 0 <= new_x < W:
                    if m[new_y][new_x] == '@':
                        break
                    elif M[new_y][new_x] == -1:
                        M[new_y][new_x] = M[y][x] + 1
                        queue.append([new_y, new_x])
                    elif M[new_y][new_x] < M[y][x] + 1:
                        break
                else:
                    break


(H, W, K) = list(map(int, input().split()))
(x1, y1, x2, y2) = list(map(int, input().split()))
(x1, y1, x2, y2) = (x1 - 1, y1 - 1, x2 - 1, y2 - 1)
m = []
for i in range(H):
    m.append(list(map(str, sys.stdin.readline().strip())))
M = [[-1] * W for i in range(H)]
bfs(M, x1, y1, x2, y2)
print(M[x2][y2])
