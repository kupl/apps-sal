import math
(n, px, py) = map(int, input().split())
(xs, ys, l) = (list(), list(), list())
for _ in range(n):
    (x, y) = map(int, input().split())
    xs.append(x - px)
    ys.append(y - py)
(x0, y0) = (xs[-1], ys[-1])
for (x, y) in zip(xs, ys):
    l.append(x * x + y * y)
    (dx, dy) = (x - x0, y - y0)
    if (x0 * dx + y0 * dy) * (x * dx + y * dy) < 0:
        x0 = x0 * y - x * y0
        l.append(x0 * x0 / (dx * dx + dy * dy))
    (x0, y0) = (x, y)
print(math.pi * (max(l) - min(l)))
