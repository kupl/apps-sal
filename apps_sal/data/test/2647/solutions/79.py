from collections import deque
h, w = map(int, input().split())
field = [input() for _ in range(h)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
white = 0
for i in range(h):
    white += field[i].count(".")
cnt = [[-1] * w for _ in range(h)]
cnt[0][0] = 0
q = deque([[0, 0]])

while q:
    y, x = q.pop()
    for dy, dx in d:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < h and 0 <= nx < w and field[ny][nx] == "." and cnt[ny][nx] < 0:
            cnt[ny][nx] = cnt[y][x] + 1
            q.appendleft([ny, nx])
        if ny == h - 1 and nx == w - 1:
            print(white - cnt[h - 1][w - 1] - 1)
            return

print(-1)
