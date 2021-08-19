from collections import defaultdict as dd, deque
from math import gcd
n = int(input())
P = [[int(x) for x in input().split()] for _ in range(n)]
L = []


def addLine(x, y, dx, dy):
    if dx < 0:
        dx *= -1
        dy *= -1
    elif dx == 0:
        if dy < 0:
            dy *= -1
    g = gcd(dx, dy)
    dx //= g
    dy //= g
    x += dx * 10 ** 9
    y += dy * 10 ** 9
    if dx:
        k = x // dx
    else:
        k = y // dy
    x -= k * dx
    y -= k * dy
    L.append((x, y, dx, dy))


for i in range(n):
    for j in range(i + 1, n):
        (xi, yi) = P[i]
        (xj, yj) = P[j]
        (dx, dy) = (xi - xj, yi - yj)
        addLine(xi, yi, dx, dy)
L = list(set(L))
res = 0
C = dd(int)
for (x, y, dx, dy) in L:
    C[dx, dy] += 1
ss = sum(C.values())
for x in list(C.values()):
    res += (ss - x) * x
print(res // 2)
