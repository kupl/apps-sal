from collections import deque
d = [[1, 0], [-1, 0], [0, -1], [0, 1]]
h, w, k = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
c = [list(input()) for i in range(h)]
visited = [[-1] * w for i in range(h)]
visited[x1 - 1][y1 - 1] = 0
Q = deque([(x1 - 1, y1 - 1)])
while Q:
    nx, ny = Q.popleft()
    if nx == x2 - 1 and ny == y2 - 1:
        print(visited[nx][ny]);return
    for dx, dy in d:
        for i in range(k):
            p, q = nx + dx * (i + 1), ny + dy * (i + 1)
            if not (0 <= p < h and 0 <= q < w) or c[p][q] == "@":
                break
            if 0 <= visited[p][q] <= visited[nx][ny]:
                break
            if visited[p][q] == -1:
                Q.append((p, q))
            visited[p][q] = visited[nx][ny] + 1
print(-1)
