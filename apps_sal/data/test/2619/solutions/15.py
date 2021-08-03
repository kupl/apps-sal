import sys
input = sys.stdin.readline
n, q, c = map(int, input().split())
g = [[[0] * 11 for i in range(101)] for i in range(101)]
for _ in range(n):
    x, y, s = map(int, input().split())
    g[x][y][s] += 1
for i in range(1, 101):
    for j in range(1, 101):
        for k in range(11):
            g[i][j][k] += g[i - 1][j][k] + g[i][j - 1][k] - g[i - 1][j - 1][k]
for _ in range(q):
    t, x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    for k in range(11):
        cnt = g[x2][y2][k] - g[x1 - 1][y2][k] - g[x2][y1 - 1][k] + g[x1 - 1][y1 - 1][k]
        ans += ((t + k) % (c + 1)) * cnt
    print(ans)
