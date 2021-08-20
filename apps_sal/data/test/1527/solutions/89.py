from collections import deque
import copy
(H, W) = map(int, input().split())
inf = 1000000000
field = []
for i in range(H):
    row = list(input())
    for j in range(len(row)):
        if row[j] == '#':
            row[j] = -1
        else:
            row[j] = inf
    field.append(row)
ans = inf


def isIn(x, y):
    if x < 0 or x >= W:
        return False
    if y < 0 or y >= H:
        return False
    return True


vector = [[0, 1], [0, -1], [1, 0], [-1, 0]]
ans = 0
for i in range(H):
    for j in range(W):
        if field[i][j] == -1:
            continue
        l = deque([[j, i]])
        f = copy.deepcopy(field)
        f[i][j] = 0
        tmp = 0
        while l:
            (x, y) = l.popleft()
            for v in vector:
                if not isIn(x + v[1], y + v[0]):
                    continue
                if f[y + v[0]][x + v[1]] <= tmp:
                    continue
                f[y + v[0]][x + v[1]] = f[y][x] + 1
                l.append([x + v[1], y + v[0]])
                tmp = max(f[y + v[0]][x + v[1]], tmp)
        ans = max(ans, tmp)
print(ans)
