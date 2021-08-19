from collections import deque


def getdistance(row, col, sw, h, w):
    maze = deque([[row, col, 0]])
    marker = [[0] * w for _ in range(h)]
    marker[row][col] = 1
    while len(maze) != 0:
        r, c, d = maze.popleft()
        if r != 0:
            if sw[r - 1][c] != "#" and marker[r - 1][c] != 1:
                marker[r - 1][c] = 1
                maze.append([r - 1, c, d + 1])
        if r != h - 1:
            if sw[r + 1][c] != "#" and marker[r + 1][c] != 1:
                marker[r + 1][c] = 1
                maze.append([r + 1, c, d + 1])
        if c != w - 1:
            if sw[r][c + 1] != "#" and marker[r][c + 1] != 1:
                marker[r][c + 1] = 1
                maze.append([r, c + 1, d + 1])
        if c != 0:
            if sw[r][c - 1] != "#" and marker[r][c - 1] != 1:
                marker[r][c - 1] = 1
                maze.append([r, c - 1, d + 1])
    return d


h, w = map(int, input().split())
sw = [input() for _ in range(h)]
ans = 0
for row in range(h):
    for col in range(w):
        if sw[row][col] == "#":
            continue
        ans = max(ans, getdistance(row, col, sw, h, w))
print(ans)
