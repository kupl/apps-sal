#!/usr/bin/env python3


from math import hypot

[n, q] = list(map(int, input().strip().split()))
xys = [tuple(map(int, input().strip().split())) for _ in range(n)]
qis = [tuple(map(int, input().strip().split())) for _ in range(q)]

dxys = [(xys[(i + 1) % n][0] - xys[i][0], xys[(i + 1) % n][1] - xys[i][1]) for i in range(n)]

S = 3 * sum((x * dy - y * dx) for (x, y), (dx, dy) in zip(xys, dxys))
Sx = sum((dx + 2 * x) * (x * dy - y * dx) for (x, y), (dx, dy) in zip(xys, dxys))
Sy = sum((dy + 2 * y) * (x * dy - y * dx) for (x, y), (dx, dy) in zip(xys, dxys))
#Sy = sum((2*dx*dy + 3*x*dx + 3*x*dy + 6*x*y)*dy for (x, y), (dx, dy) in zip(xys, dxys))
for p in [2, 3]:
    while S % p == Sx % p == Sy % p == 0:
        S //= p
        Sx //= p
        Sy //= p

xyms = [(S * x - Sx, S * y - Sy) for x, y in xys]
hs = [hypot(x, y) for x, y in xyms]


def to_coord(x, y):
    return (x + Sx) / S, (y + Sy) / S


hangs = (0, 1)
hang_on = None
cx, cy = 0.0, 0.0

# hang on u


def get_v(v):
    if hang_on is None:
        return xyms[v]
    else:
        ux, uy = xyms[hang_on]
        vx, vy = xyms[v]
        h = hs[hang_on]
        return ((uy * vx - ux * vy) / h, (ux * vx + uy * vy) / h)

# def ss(v1, v2):
#	return tuple(vi + vj for vi, vj in zip(v1, v2))

# def disp():
#	print ('hangs on', hang_on, 'of', hangs)
#	print ('center', to_coord(cx, cy))
#	print ({i: to_coord(*ss(get_v(i), (cx, cy))) for i in range(n)})


# disp()
for qi in qis:
    if qi[0] == 1:
        _, f, t = qi  # 1-indexation
        s = hangs[1 - hangs.index(f - 1)]
        dx, dy = get_v(s)
        cx += dx
        cy += dy - hs[s]
        hang_on = s
        hangs = (s, t - 1)
#		print ('{} --> {}'.format(f - 1, t - 1))
#		disp()
    else:
        _, v = qi  # 1-indexation
        dx, dy = get_v(v - 1)
        print(*to_coord(cx + dx, cy + dy))
