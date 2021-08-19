import queue


def bfs(maze, h, w, sy, sx):
    dist = [[-1 for _ in range(w)] for _ in range(h)]
    q = queue.deque([[sy, sx]])
    dist[sy][sx] = 0
    while q:
        (y, x) = q.popleft()
        for (dy, dx) in d:
            (ny, nx) = (y + dy, x + dx)
            if 0 <= ny < h and 0 <= nx < w and (dist[ny][nx] == -1) and (maze[ny][nx] != '#'):
                dist[ny][nx] = dist[y][x] + 1
                q.append([ny, nx])
    return max([max(i) for i in dist])


(h, w) = map(int, input().split())
a = [input() for _ in range(h)]
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ans = 0
for sy in range(h):
    for sx in range(w):
        if a[sy][sx] != '#':
            ans = max(ans, bfs(a, h, w, sy, sx))
print(ans)
