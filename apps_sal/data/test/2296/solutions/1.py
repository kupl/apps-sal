from math import hypot
[n, q] = list(map(int, input().strip().split()))
xys = [tuple(map(int, input().strip().split())) for _ in range(n)]
qis = [tuple(map(int, input().strip().split())) for _ in range(q)]
dxys = [(xys[(i + 1) % n][0] - xys[i][0], xys[(i + 1) % n][1] - xys[i][1]) for i in range(n)]
S = 3 * sum((x * dy - y * dx for ((x, y), (dx, dy)) in zip(xys, dxys)))
Sx = sum(((dx + 2 * x) * (x * dy - y * dx) for ((x, y), (dx, dy)) in zip(xys, dxys)))
Sy = sum(((dy + 2 * y) * (x * dy - y * dx) for ((x, y), (dx, dy)) in zip(xys, dxys)))
for p in [2, 3]:
    while S % p == Sx % p == Sy % p == 0:
        S //= p
        Sx //= p
        Sy //= p
xyms = [(S * x - Sx, S * y - Sy) for (x, y) in xys]
hs = [hypot(x, y) for (x, y) in xyms]


def to_coord(x, y):
    return ((x + Sx) / S, (y + Sy) / S)


hangs = (0, 1)
hang_on = None
(cx, cy) = (0.0, 0.0)


def get_v(v):
    if hang_on is None:
        return xyms[v]
    else:
        (ux, uy) = xyms[hang_on]
        (vx, vy) = xyms[v]
        h = hs[hang_on]
        return ((uy * vx - ux * vy) / h, (ux * vx + uy * vy) / h)


for qi in qis:
    if qi[0] == 1:
        (_, f, t) = qi
        s = hangs[1 - hangs.index(f - 1)]
        (dx, dy) = get_v(s)
        cx += dx
        cy += dy - hs[s]
        hang_on = s
        hangs = (s, t - 1)
    else:
        (_, v) = qi
        (dx, dy) = get_v(v - 1)
        print(*to_coord(cx + dx, cy + dy))
