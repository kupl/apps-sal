from collections import deque


def bfs(maze, visited, sy, sx, gy, gx):
    queue = deque([[sy, sx]])
    visited[sy][sx] = 0
    while queue:
        (y, x) = queue.popleft()
        if [y, x] == [gy, gx]:
            return visited[y][x]
        for (j, k) in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            l = 1
            while True:
                (new_y, new_x) = (y + j * l, x + k * l)
                if 0 <= new_y < H and 0 <= new_x < W:
                    if maze[new_y][new_x] == '@':
                        break
                    elif visited[new_y][new_x] == -1:
                        visited[new_y][new_x] = visited[y][x] + 1
                        queue.append([new_y, new_x])
                    elif visited[new_y][new_x] < visited[y][x] + 1:
                        break
                else:
                    break
                l += 1
                if l == K + 1:
                    break


(H, W, K) = map(int, input().split())
(x1, y1, x2, y2) = map(int, input().split())
(x1, y1, x2, y2) = (x1 - 1, y1 - 1, x2 - 1, y2 - 1)
C = [0] * H
for i in range(H):
    C[i] = str(input())
visited = [[-1] * W for i in range(H)]
bfs(C, visited, x1, y1, x2, y2)
print(visited[x2][y2])
