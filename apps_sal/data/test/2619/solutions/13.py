import sys
from collections import defaultdict
input = sys.stdin.readline
(n, q, c) = map(int, input().split())
d = defaultdict(lambda: [0] * 11)
for _ in range(n):
    (x, y, s) = map(int, input().split())
    if (x, y) not in d:
        d[x, y] = [0] * 11
    d[x, y][s] += 1
g = [[[0] * 11 for i in range(101)] for i in range(101)]
g[1][1] = d[1, 1]
for i in range(1, 101):
    for j in range(1, 101):
        if i == 1 and j == 1:
            continue
        for k in range(11):
            if i == 1:
                g[i][j][k] = g[i][j - 1][k] + d[i, j][k]
            elif j == 1:
                g[i][j][k] = g[i - 1][j][k] + d[i, j][k]
            else:
                g[i][j][k] = g[i - 1][j][k] + g[i][j - 1][k] - g[i - 1][j - 1][k] + d[i, j][k]
for _ in range(q):
    (t, x1, y1, x2, y2) = map(int, input().split())
    ans = 0
    for k in range(11):
        cnt = g[x2][y2][k] - g[x1 - 1][y2][k] - g[x2][y1 - 1][k] + g[x1 - 1][y1 - 1][k]
        ans += (t + k) % (c + 1) * cnt
    print(ans)
