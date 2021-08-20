from copy import deepcopy
from collections import deque
(h, w) = map(int, input().split())
s = [['#'] * (w + 2) for i in range(h + 2)]
for i in range(h):
    x = input()
    for j in range(w):
        s[i + 1][j + 1] = x[j]
ans = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if s[i][j] != '#':
            maze = deepcopy(s)
            maze[i][j] = 0
            queue = deque([[i, j]])
            while queue:
                (x, y) = queue.popleft()
                for (a, b) in ([0, -1], [0, 1], [1, 0], [-1, 0]):
                    (nh, nw) = (x + a, y + b)
                    if maze[nh][nw] == '.':
                        maze[nh][nw] = maze[x][y] + 1
                        queue.append([nh, nw])
            l = 0
            for x in range(1, h + 1):
                for y in range(1, w + 1):
                    if maze[x][y] != '#':
                        l = max(l, maze[x][y])
            ans = max(ans, l)
print(ans)
