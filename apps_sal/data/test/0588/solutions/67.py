from math import hypot
N = int(input())
engines = [tuple(map(int, input().split())) for _ in range(N)]


def dot(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2


def cross(x1, y1, x2, y2):
    return x1 * y2 - y1 * x2


def getDistMax(xBase, yBase):
    (x1s, y1s, x2s, y2s) = ([], [], [], [])
    (x, y) = (0, 0)
    for (dx, dy) in engines:
        d = dot(xBase, yBase, dx, dy)
        if d > 0:
            (x, y) = (x + dx, y + dy)
        elif d == 0:
            c = cross(xBase, yBase, dx, dy)
            if c > 0:
                x1s.append(dx)
                y1s.append(dy)
            else:
                x2s.append(dx)
                y2s.append(dy)
    ans = max(hypot(x, y), hypot(x + sum(x1s), y + sum(y1s)), hypot(x + sum(x2s), y + sum(y2s)))
    return ans


ans = 0
for (x, y) in engines:
    ds = []
    ds.append(getDistMax(x, y))
    ds.append(getDistMax(-y, x))
    ds.append(getDistMax(-x, -y))
    ds.append(getDistMax(y, -x))
    ans = max(ans, max(ds))
print(ans)
