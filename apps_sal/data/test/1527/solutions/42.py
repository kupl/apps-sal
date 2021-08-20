from collections import deque
import copy
(H, W) = map(int, input().split())
MAP = [list(input()) for y in range(H)]


def Maze(_x, _y):
    MAP2 = copy.deepcopy(MAP)
    q = deque([[_x, _y]])
    MAP2[_y][_x] = 0
    while q:
        xy = q.popleft()
        for d in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            (x2, y2) = (xy[0] + d[0], xy[1] + d[1])
            if x2 < 0 or y2 < 0 or x2 >= W or (y2 >= H):
                continue
            if MAP2[y2][x2] == '.':
                q.append([x2, y2])
                MAP2[y2][x2] = MAP2[xy[1]][xy[0]] + 1
    maxM = 0
    for y in range(H):
        for x in range(W):
            if type(MAP2[y][x]) == int:
                maxM = max(maxM, MAP2[y][x])
    return maxM


ans = 0
for y in range(H):
    for x in range(W):
        if MAP[y][x] == '.':
            ans = max(ans, Maze(x, y))
print(ans)
