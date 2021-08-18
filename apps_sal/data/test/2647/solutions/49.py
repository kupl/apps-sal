
from collections import deque


H, W = list(map(int, input().split()))
grid = [list(input()) for _ in range(H)]
visited = [[-1] * W for _ in range(H)]
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = deque()
q.append((0, 0))
visited[0][0] = 0

while q:
    y, x = q.popleft()

    for dy, dx in moves:
        moved_y = y + dy
        moved_x = x + dx

        if moved_y < 0 or H - 1 < moved_y or moved_x < 0 or W - 1 < moved_x:
            continue
        if grid[moved_y][moved_x] == '
        continue
        if visited[moved_y][moved_x] != -1:
            continue

        visited[moved_y][moved_x] = visited[y][x] + 1
        q.append((moved_y, moved_x))

min_route = visited[H - 1][W - 1]

if min_route == -1:
    answer = -1
else:
    total_white = 0
    for row in grid:
        total_white += row.count('.')

    answer = total_white - min_route - 1

print(answer)
