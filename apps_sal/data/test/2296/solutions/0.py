import math


def getCoordinate(gx, gy, alpha, x, y):
    x1 = gx + x * math.cos(alpha) - y * math.sin(alpha)
    y1 = gy + x * math.sin(alpha) + y * math.cos(alpha)
    return (x1, y1)


def getAngle(gx, gy, x, y):
    x = x - gx
    y = y - gy
    cos = x / math.sqrt(x ** 2 + y ** 2)
    alpha = math.acos(cos)
    if y < 0:
        alpha = -alpha
    return math.pi / 2 - alpha


(n, q) = list(map(int, input().split(' ')))
x = [0] * n
y = [0] * n
for i in range(n):
    (x[i], y[i]) = list(map(int, input().split(' ')))
r = [0] * q
f = [0] * q
t = [0] * q
v = [0] * q
for i in range(q):
    l = list(map(int, input().split(' ')))
    r[i] = l[0]
    if r[i] == 1:
        f[i] = l[1] - 1
        t[i] = l[2] - 1
    else:
        v[i] = l[1] - 1
gx = 0
gy = 0
s = 0
for i in range(n):
    ip = i + 1
    if ip == n:
        ip = 0
    ds = x[i] * y[ip] - x[ip] * y[i]
    s += ds
    gx += (x[i] + x[ip]) * ds
    gy += (y[i] + y[ip]) * ds
s /= 2
gx /= 6 * s
gy /= 6 * s
angles = [0] * n
for i in range(n):
    angles[i] = getAngle(gx, gy, x[i], y[i])
for i in range(n):
    x[i] -= gx
    y[i] -= gy
alpha = 0
fix = {0, 1}
for i in range(q):
    if r[i] == 2:
        (currX, currY) = getCoordinate(gx, gy, alpha, x[v[i]], y[v[i]])
        print('%.6f %.6f' % (currX, currY))
    else:
        if len(fix) == 2:
            fix.remove(f[i])
        for j in fix:
            (currX, currY) = getCoordinate(gx, gy, alpha, x[j], y[j])
            alpha = angles[j]
            (gx, gy) = (currX, currY - math.sqrt(x[j] ** 2 + y[j] ** 2))
        fix.add(t[i])
