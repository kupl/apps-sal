import sys
import operator
from collections import deque, Counter

input = sys.stdin.readline
h, w = map(int, input().split())
sx, sy = 0, 0
gx, gy = h - 1, w - 1
s = [list(input()) for _ in range(h)]
c = []
for a in s:
    c += a
c = Counter(c)
white = c["."]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[-1] * w for _ in range(h)]


def bfs(x, y):
    queue = deque([[x, y]])
    visited[x][y] = 0
    while queue:

        x, y = queue.popleft()
        if [x, y] == [gx, gy]:
            return visited[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < h and ny >= 0 and ny < w and s[nx][ny] == "." and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])


bfs(sx, sy)
print(white - visited[gx][gy] - 1 if visited[gx][gy] != -1 else -1)
