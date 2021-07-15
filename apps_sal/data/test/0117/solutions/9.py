import bisect
import sys

lower_bound = bisect.bisect_left
upper_bound = bisect.bisect_right
INF = 0x3fffffff

n, m = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(m)]

X = {-INF, INF}
Y = {-INF, INF}
for i in a:
    Y.add(i[2])
for i in b:
    X.add(i[0])

X = list(sorted(X))
Y = list(sorted(Y))
n = len(X) - 1
m = len(Y) - 1
wallx = [[False] * m for i in range(n)]
wally = [[False] * m for i in range(n)]

for x1, x2, y1 in a:
    x1 = lower_bound(X, x1)
    y1 = lower_bound(Y, y1)
    x2 = upper_bound(X, x2) - 1
    for i in range(x1, x2):
        wally[i][y1] = True

for x1, y1, y2 in b:
    x1 = lower_bound(X, x1)
    y1 = lower_bound(Y, y1)
    y2 = upper_bound(Y, y2) - 1
    for i in range(y1, y2):
        wallx[x1][i] = True

cow = [[False] * m for i in range(n)]
cx = upper_bound(X, 0) - 1
cy = upper_bound(Y, 0) - 1
cow[cx][cy] = True
q = [(cx, cy)]
ans = 0

while q:
    x, y = q.pop()
    if not x or not y:
        print("INF")
        return
    ans += (X[x + 1] - X[x]) * (Y[y + 1] - Y[y])
    if x and not wallx[x][y] and not cow[x - 1][y]:
        cow[x - 1][y] = True
        q.append((x - 1, y))
    if y and not wally[x][y] and not cow[x][y - 1]:
        cow[x][y - 1] = True
        q.append((x, y - 1))
    if x + 1 < n and not wallx[x + 1][y] and not cow[x + 1][y]:
        cow[x + 1][y] = True
        q.append((x + 1, y))
    if y + 1 < m and not wally[x][y + 1] and not cow[x][y + 1]:
        cow[x][y + 1] = True
        q.append((x, y + 1))

print(ans)

