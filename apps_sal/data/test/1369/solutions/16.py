from math import sqrt


def colinear(x1, y1, x2, y2, x3, y3):
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    if a == 0:
        return True
    else:
        return False


def distance(x1, y1, x2, y2):
    xd = (x1 - x2) ** 2
    yd = (y1 - y2) ** 2
    return sqrt(xd + yd)


def check(cx, cy, r, x, y, n):
    for i in range(n):
        d = distance(cx, cy, x[i], y[i])
        if d - r > 0.1:
            return False
    return True


def circlebydiaendpoints(x1, y1, x2, y2):
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    r = distance(cx, cy, x1, y1)
    return (cx, cy, r)


def makeCircumcircle(x1, y1, x2, y2, x3, y3):
    ox = (min(min(x1, x2), x3) + max(min(x1, x2), x3)) / 2
    oy = (min(min(y1, y2), y3) + max(min(y1, y2), y3)) / 2
    ax = x1 - ox
    ay = y1 - oy
    bx = x2 - ox
    by = y2 - oy
    cx = x3 - ox
    cy = y3 - oy
    d = (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)) * 2
    x = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    y = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    cx = ox + x
    cy = oy + y
    r = max(max(distance(cx, cy, x1, y1), distance(cx, cy, x2, y2)), distance(cx, cy, x3, y3))
    return (cx, cy, r)


def main():
    n = int(input())
    x = []
    y = []
    for _ in range(n):
        (a, b) = input().split(' ')
        a = float(a)
        b = float(b)
        x.append(a)
        y.append(b)
    ans = -1
    for i in range(n - 1):
        for j in range(i + 1, n):
            (cx, cy, r) = circlebydiaendpoints(x[i], y[i], x[j], y[j])
            if check(cx, cy, r, x, y, n):
                if ans == -1:
                    ans = r
                elif ans > r:
                    ans = r
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if colinear(x[i], y[i], x[j], y[j], x[k], y[k]):
                    continue
                else:
                    (cx, cy, r) = makeCircumcircle(x[i], y[i], x[j], y[j], x[k], y[k])
                    if check(cx, cy, r, x, y, n):
                        if ans == -1:
                            ans = r
                        elif ans > r:
                            ans = r
    print(ans)


def __starting_point():
    main()


__starting_point()
