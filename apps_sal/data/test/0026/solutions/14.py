from math import log


def lbig(x, y, z, f):
    if x == 1.0:
        return 0.0

    w = 1.0
    if x < 1.0:
        x = 1.0 / x

    if f == True:
        return w * (z * log(y) + log(log(x)))

    return w * (log(y) + log(z) + log(log(x)))


def rets(x, y, z, xs, ys, zs, n):
    xss = [
        (lbig(x, y, z, True), xs + '^' + ys + '^' + zs, n + 1),
        (lbig(x, z, y, True), xs + '^' + zs + '^' + ys, n + 2),
        (lbig(x, y, z, False), '(' + xs + '^' + ys + ')^' + zs, n + 3),
        (lbig(x, z, y, False), '(' + xs + '^' + zs + ')^' + ys, n + 4),
    ]
    return xss


x, y, z = list(map(float, input().split()))
ans = ''
if x <= 1.0 and y <= 1.0 and z <= 1.0:
    xss = [
        (x**(y**z), 'x^y^z', 1),
        (x**(z**y), 'x^z^y', 2),
        (x**(y * z), '(x^y)^z', 3),
        (x**(z * y), '(x^z)^y', 4),
    ]
    yss = [
        (y**(x**z), 'y^x^z', 5),
        (y**(z**x), 'y^z^x', 6),
        (y**(x * z), '(y^x)^z', 7),
        (y**(z * x), '(y^z)^x', 8),
    ]
    zss = [
        (z**(x**y), 'z^x^y', 9),
        (z**(y**x), 'z^y^x', 10),
        (z**(x * y), '(z^x)^y', 11),
        (z**(y * x), '(z^y)^x', 12),
    ]
    anss = sorted(xss + yss + zss, key=lambda x: (x[0], -x[2]))
    ans = anss[-1][1]
else:
    xss = []
    yss = []
    zss = []
    if x > 1.0:
        xss = rets(x, y, z, 'x', 'y', 'z', 0)
    if y > 1.0:
        yss = rets(y, x, z, 'y', 'x', 'z', 4)
    if z > 1.0:
        zss = rets(z, x, y, 'z', 'x', 'y', 8)
    anss = sorted(xss + yss + zss, key=lambda x: (x[0], -x[2]))
    # print(anss)
    ans = anss[-1][1]

print(ans)
