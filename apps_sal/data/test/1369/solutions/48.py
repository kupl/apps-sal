from math import hypot

N = int(input())
pts = [tuple(map(int, input().split())) for _ in range(N)]


def getIntersectionLL(a1, b1, c1, a2, b2, c2):
    v = a1 * b2 - a2 * b1
    if v == 0:
        return (None, None)
    else:
        return ((b1 * c2 - b2 * c1) / v, (-a1 * c2 + a2 * c1) / v)


def getPerpendicularBisector(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    xM, yM = (x1 + x2) / 2, (y1 + y2) / 2
    return (-dx, -dy, dx * xM + dy * yM)


def getCircumcenter(x1, y1, x2, y2, x3, y3):
    a12, b12, c12 = getPerpendicularBisector(x1, y1, x2, y2)
    a13, b13, c13 = getPerpendicularBisector(x1, y1, x3, y3)
    intLL = getIntersectionLL(a12, b12, c12, a13, b13, c13)
    return intLL


ans = float('inf')
for i in range(N):
    x1, y1 = pts[i]
    for j in range(i + 1, N):
        x2, y2 = pts[j]
        xC, yC = (x1 + x2) / 2, (y1 + y2) / 2
        dist = max([hypot(x - xC, y - yC) for x, y in pts])
        ans = min(ans, dist)

for i in range(N):
    x1, y1 = pts[i]
    for j in range(i + 1, N):
        x2, y2 = pts[j]
        for k in range(j + 1, N):
            x3, y3 = pts[k]
            xC, yC = getCircumcenter(x1, y1, x2, y2, x3, y3)
            if xC is None: continue
            dist = max([hypot(x - xC, y - yC) for x, y in pts])
            ans = min(ans, dist)

print(ans)
