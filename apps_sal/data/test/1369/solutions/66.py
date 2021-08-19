from math import sqrt
N = int(input())
THRE = 1e-07
ps = []
for _ in range(N):
    (x, y) = list(map(int, input().split()))
    ps.append((x, y))


def circleThrough2Points(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return (None, None, None)
    px = (x1 + x2) / 2
    py = (y1 + y2) / 2
    r = (px - x1) ** 2 + (py - y1) ** 2
    return (px, py, r)


def circleThrough3Points(x1, y1, x2, y2, x3, y3):
    (a, b, c, d, e, f) = (x1, y1, x2, y2, x3, y3)
    (a2, b2, c2, d2, e2, f2) = (a * a, b * b, c * c, d * d, e * e, f * f)
    py_1 = 2 * (e - a) * (b - d) - 2 * (c - a) * (b - f)
    if py_1 == 0:
        return (None, None, None)
    py_2 = (e - a) * (a2 + b2 - c2 - d2) - (c - a) * (a2 + b2 - e2 - f2)
    py = py_2 / py_1
    if a != c:
        px = (2 * (b - d) * py - a2 - b2 + c2 + d2) / (2 * (c - a))
    else:
        px = (2 * (b - f) * py - a2 - b2 + e2 + f2) / (2 * (e - a))
    r = (px - a) ** 2 + (py - b) ** 2
    return (px, py, r)


ans = float('inf')
for i in range(N):
    (x1, y1) = ps[i]
    for j in range(i + 1, N):
        (x2, y2) = ps[j]
        (px, py, r) = circleThrough2Points(x1, y1, x2, y2)
        if r is not None:
            if all([(px - x) ** 2 + (py - y) ** 2 <= r + THRE for (x, y) in ps]):
                ans = ans if ans < r else r
        for k in range(j + 1, N):
            (x3, y3) = ps[k]
            (px, py, r) = circleThrough3Points(x1, y1, x2, y2, x3, y3)
            if r is not None:
                if all([(px - x) ** 2 + (py - y) ** 2 <= r + THRE for (x, y) in ps]):
                    ans = ans if ans < r else r
print(sqrt(ans))
