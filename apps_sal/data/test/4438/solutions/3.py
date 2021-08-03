import sys


def minp():
    return sys.stdin.readline().strip()


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


n = int(minp())
a = [None] * n
for i in range(n):
    x, y = list(map(int, minp().split()))
    a[i] = (max(x, y), x, -y)
a.sort()
# print(a)
p = [None] * 2
d = [None] * 2
p[0] = [None] * (n + 1)
p[1] = [None] * (n + 1)
d[0] = [None] * (n + 1)
d[1] = [None] * (n + 1)
d[0][0] = 0
d[1][0] = 0
p[0][0] = (0, 0, 0)
p[1][0] = (0, 0, 0)
i = 0
k = 1
while i < n:
    x = a[i]
    xx = x[0]
    j = i + 1
    while j < n and a[j][0] == xx:
        j += 1
    y = a[j - 1]
    p0 = p[0][k - 1]
    p1 = p[1][k - 1]
    d0 = d[0][k - 1]
    d1 = d[1][k - 1]
    dd = dist(x[1], x[2], y[1], y[2])
    d2 = dist(p0[1], p0[2], x[1], x[2])
    d3 = dist(p1[1], p1[2], x[1], x[2])
    d[0][k] = min(d0 + d2, d1 + d3) + dd
    p[0][k] = y
    d2 = dist(p0[1], p0[2], y[1], y[2])
    d3 = dist(p1[1], p1[2], y[1], y[2])
    d[1][k] = min(d0 + d2, d1 + d3) + dd
    p[1][k] = x
    k += 1
    i = j
print(min(d[0][k - 1], d[1][k - 1]))
