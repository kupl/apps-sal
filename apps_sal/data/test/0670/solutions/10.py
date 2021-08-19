import math


def lll(a, b):
    return math.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)


def III(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


(a, b, c) = map(int, input().split())
(x1, y1, x2, y2) = map(int, input().split())
g = [[]] * 8
for i in range(8):
    g[i] = [float('inf')] * 8
p = [(x1, y1), (x1, y2), (x2, y2), (x2, y1)]
l = []
if a != 0 and b != 0:
    l = [(x1, (-a * x1 - c) / b), ((-b * y1 - c) / a, y1), (x2, (-a * x2 - c) / b), ((-b * y2 - c) / a, y2)]
else:
    l = [(x1, y1), (x1, y1), (x1, y1), (x1, y1)]
for i in range(4):
    for j in range(4):
        g[i][4 + j] = g[4 + j][i] = III(p[i], l[j])
        if i != j:
            g[i][j] = g[j][i] = III(p[i], p[j])
            g[4 + i][4 + j] = g[4 + j][4 + i] = lll(l[i], l[j])
ls = [float('inf')] * 8
ls[0] = 0
qu = [0]
while len(qu) > 0:
    i = qu[0]
    qu = qu[1:]
    for j in range(8):
        if ls[i] + g[i][j] < ls[j]:
            ls[j] = ls[i] + g[i][j]
            if not j in qu:
                qu += [j]
print(ls[2])
