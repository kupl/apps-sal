from collections import deque
(h, w) = map(int, input().split())
s = [list(input()) for _ in range(h)]
dots = sum([v.count('.') for v in s])
visited = [[-1] * w for _ in range(h)]
q = deque([[0, 0]])
visited[0][0] = 1
while q:
    (y, x) = q.popleft()
    if y == h - 1 and x == w - 1:
        break
    for (i, j) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        (ny, nx) = (y + i, x + j)
        if not 0 <= ny < h or not 0 <= nx < w or s[ny][nx] == '#':
            continue
        elif visited[ny][nx] == -1:
            visited[ny][nx] = visited[y][x] + 1
            q.append([ny, nx])
if visited[h - 1][w - 1] != -1:
    print(dots - visited[h - 1][w - 1])
else:
    print(-1)
