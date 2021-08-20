from collections import deque
(h, w) = map(int, input().split())
maze = []
for _ in range(h):
    maze.append(input())
ans = 0
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for i in range(h):
    for j in range(w):
        if maze[i][j] == '.':
            dist = [[99999999] * w for _ in range(h)]
            dq = deque()
            y = i
            x = j
            d = 0
            dist[y][x] = 0
            dq.append((y, x, d))
            while len(dq):
                (y, x, d) = dq.popleft()
                for m in move:
                    if 0 <= x + m[0] < w and 0 <= y + m[1] < h and (dist[y + m[1]][x + m[0]] > d + 1) and (maze[y + m[1]][x + m[0]] == '.'):
                        dist[y + m[1]][x + m[0]] = d + 1
                        dq.append((y + m[1], x + m[0], d + 1))
            ans = max(ans, d)
print(ans)
