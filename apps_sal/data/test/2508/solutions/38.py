from collections import deque


def bfs(visited, sy, sx, gy, gx):
    queue = deque([[sy, sx]])
    visited[sy][sx] = 0
    while queue:
        (y, x) = queue.popleft()
        if [y, x] == [gy, gx]:
            return visited[y][x]
        for (dx, dy) in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            for k in range(1, K + 1):
                new_x = x + dx * k
                new_y = y + dy * k
                if 0 <= new_y < H and 0 <= new_x < W:
                    if m[new_y][new_x] == '@':
                        break
                    elif visited[new_y][new_x] == -1:
                        visited[new_y][new_x] = visited[y][x] + 1
                        queue.append([new_y, new_x])
                    elif visited[new_y][new_x] < visited[y][x] + 1:
                        break
                else:
                    break


(H, W, K) = list(map(int, input().split()))
(x1, y1, x2, y2) = list(map(int, input().split()))
(x1, y1, x2, y2) = (x1 - 1, y1 - 1, x2 - 1, y2 - 1)
m = []
for i in range(H):
    m.append(str(input()))
visited = [[-1] * W for i in range(H)]
bfs(visited, x1, y1, x2, y2)
print(visited[x2][y2])
