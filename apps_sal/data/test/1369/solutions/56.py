from math import hypot
N = int(input())
pts = [tuple(map(int, input().split())) for _ in range(N)]
EPS = 10 ** (-10)


def isLE(a, b):
    return not a > b + EPS


def getIntersectionLCs_L(a, b, c, xC, yC, r):
    e = a * xC + b * yC + c
    ab2 = a ** 2 + b ** 2
    v = r ** 2 * ab2 - e ** 2
    if v < 0:
        return []
    elif v == 0:
        xP = xC + -a * e / ab2
        yP = yC + -b * e / ab2
        return [(xP, yP)]
    else:
        v = v ** 0.5
        xP1 = xC + (-a * e + b * v) / ab2
        yP1 = yC + (-b * e - a * v) / ab2
        xP2 = xC + (-a * e - b * v) / ab2
        yP2 = yC + (-b * e + a * v) / ab2
        return [(xP1, yP1), (xP2, yP2)]


def getIntersectionCCs(x1, y1, r1, x2, y2, r2):
    (xC, yC) = (x2 - x1, y2 - y1)
    c = -(xC ** 2 + yC ** 2 + r1 ** 2 - r2 ** 2) / 2
    intCCs = getIntersectionLCs_L(xC, yC, c, 0, 0, r1)
    intCCs = [(x1 + x, y1 + y) for (x, y) in intCCs]
    return intCCs


def isOK(r):
    for i in range(N):
        (x1, y1) = pts[i]
        for j in range(i + 1, N):
            (x2, y2) = pts[j]
            intCCs = getIntersectionCCs(x1, y1, r, x2, y2, r)
            for (xC, yC) in intCCs:
                dist = max([hypot(x - xC, y - yC) for (x, y) in pts])
                if isLE(dist, r):
                    return True
    return False


(ng, ok) = (0, 2000)
while abs(ok - ng) > 10 ** (-12):
    mid = (ng + ok) / 2
    if isOK(mid):
        ok = mid
    else:
        ng = mid
print(ok)
