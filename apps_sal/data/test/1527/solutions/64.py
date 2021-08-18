
from collections import deque

H, W = list(map(int, input().split()))
maze = [list(input()) for i in range(H)]


def bfs(sx, sy):
    result = 0
    count = [[-1] * W for i in range(H)]
    count[sx][sy] = 0
    d = deque()
    d.append((sx, sy))
    while d:
        x, y = d.popleft()
        result = count[x][y]
        for i, j in ([1, 0], [0, 1], [-1, 0], [0, -1]):
            tx, ty = x + i, y + j
            if (
                not (0 <= tx < H) or
                not (0 <= ty < W) or
                maze[tx][ty] == "
                count[tx][ty] != -1
            ):
                continue
            else:
                count[tx][ty] = count[x][y] + 1
                d.append((tx, ty))
    return result


ans = 0
for i in range(W):
    for j in range(H):
        if maze[j][i] == ".":
            ans = max(ans, bfs(j, i))
print(ans)
