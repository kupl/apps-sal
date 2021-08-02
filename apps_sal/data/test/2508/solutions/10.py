from collections import deque
import sys
input = sys.stdin.readline

H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
MAP = [list(input().strip()) for i in range(H)]

for i in range(H):
    for j in range(W):
        if MAP[i][j] == ".":
            MAP[i][j] = 1 << 30
        else:
            MAP[i][j] = -1

Q = deque()
Q.append((x1 - 1, y1 - 1))
MAP[x1 - 1][y1 - 1] = 0

while Q:
    x, y = Q.pop()

    for i in range(1, K + 1):
        if 0 <= x + i < H and 0 <= y < W and (MAP[x + i][y] == 1 << 30 or MAP[x + i][y] > MAP[x][y]):
            if MAP[x + i][y] == 1 << 30:
                MAP[x + i][y] = MAP[x][y] + 1
                Q.appendleft((x + i, y))
        else:
            break

    for i in range(1, K + 1):
        if 0 <= x - i < H and 0 <= y < W and (MAP[x - i][y] == 1 << 30 or MAP[x - i][y] > MAP[x][y]):
            if MAP[x - i][y] == 1 << 30:
                MAP[x - i][y] = MAP[x][y] + 1
                Q.appendleft((x - i, y))
        else:
            break

    for i in range(1, K + 1):
        if 0 <= x < H and 0 <= y + i < W and (MAP[x][y + i] == 1 << 30 or MAP[x][y + i] > MAP[x][y]):
            if MAP[x][y + i] == 1 << 30:
                MAP[x][y + i] = MAP[x][y] + 1
                Q.appendleft((x, y + i))
        else:
            break

    for i in range(1, K + 1):
        if 0 <= x < H and 0 <= y - i < W and (MAP[x][y - i] == 1 << 30 or MAP[x][y - i] > MAP[x][y]):
            if MAP[x][y - i] == 1 << 30:
                MAP[x][y - i] = MAP[x][y] + 1
                Q.appendleft((x, y - i))
        else:
            break
if MAP[x2 - 1][y2 - 1] == 1 << 30:
    print(-1)
else:
    print(MAP[x2 - 1][y2 - 1])
