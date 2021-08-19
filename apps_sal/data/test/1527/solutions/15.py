from copy import deepcopy
from collections import deque
(h, w) = map(int, input().split())
s = [['#'] * (w + 2)] + [['#'] + list(input()) + ['#'] for i in range(h)] + [['#'] * (w + 2)]
ans = 0
for i in range(1, h + 1):
    for j in range(1, w + 1):
        t = deepcopy(s)
        if s[i][j] == '#':
            continue
        a = deque([[i, j, 0]])
        while len(a) > 0:
            (x, y, cnt) = a.popleft()
            t[x][y] = '#'
            if t[x - 1][y] == '.':
                a.append([x - 1, y, cnt + 1])
                t[x - 1][y] = '#'
            if t[x + 1][y] == '.':
                a.append([x + 1, y, cnt + 1])
                t[x + 1][y] = '#'
            if t[x][y - 1] == '.':
                a.append([x, y - 1, cnt + 1])
                t[x][y - 1] = '#'
            if t[x][y + 1] == '.':
                a.append([x, y + 1, cnt + 1])
                t[x][y + 1] = '#'
        ans = max(ans, cnt)
print(ans)
