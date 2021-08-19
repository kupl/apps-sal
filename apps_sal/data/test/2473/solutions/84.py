from itertools import combinations
(n, k) = map(int, input().split())
xy = [list(map(int, input().split())) + [i] for i in range(n)]
x_order = sorted(xy)
y_order = sorted(xy, key=lambda x: x[1])
pos = [[None] * 2 for _ in range(n)]
for (i, (x, y, j)) in enumerate(x_order):
    pos[j][0] = i
for (i, (x, y, j)) in enumerate(y_order):
    pos[j][1] = i
count = [[0] * (n + 1) for _ in range(n + 1)]
for (x, y) in pos:
    count[y + 1][x + 1] += 1
for i in range(n + 1):
    for j in range(1, n + 1):
        count[i][j] += count[i][j - 1]
for i in range(n + 1):
    for j in range(1, n + 1):
        count[j][i] += count[j - 1][i]
ans = float('inf')
for (x1, x2) in combinations(range(1, n + 1), 2):
    for (y1, y2) in combinations(range(1, n + 1), 2):
        if count[y2][x2] - count[y2][x1 - 1] - count[y1 - 1][x2] + count[y1 - 1][x1 - 1] >= k:
            S = (x_order[x2 - 1][0] - x_order[x1 - 1][0]) * (y_order[y2 - 1][1] - y_order[y1 - 1][1])
            ans = min(ans, S)
print(ans)
