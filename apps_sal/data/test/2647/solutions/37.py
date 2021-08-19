from collections import deque

inf = 10**10

h, w = map(int, input().split())
field = [input() for _ in range(h)]

length = [[inf for j in range(w)]for i in range(h)]
visited = [[0 for j in range(w)]for i in range(h)]

move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

que = deque([])
que.append([0, 0])
length[0][0] = 1  # １スタート
visited[0][0] = 1

white = 0

for i in range(h):
    white += field[i].count(".")

while que:
    y, x = que.popleft()

    for i, j in move:
        ny, nx = y + i, x + j

        if ny < 0 or ny >= h or nx < 0 or nx >= w:
            continue
        elif field[ny][nx] == "#":
            continue
        elif visited[ny][nx] == 1:
            continue

        visited[ny][nx] = 1
        que.append([ny, nx])
        length[ny][nx] = length[y][x] + 1

if length[h - 1][w - 1] == inf:
    print(-1)
else:
    print(white - length[h - 1][w - 1])  # 白の総数から最小距離分引く
