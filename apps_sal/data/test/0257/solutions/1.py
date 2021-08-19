from math import hypot


def solve():
    (N, K) = list(map(int, input().split()))
    (xs, ys, cs) = ([], [], [])
    for _ in range(N):
        (x, y, c) = list(map(int, input().split()))
        xs.append(x)
        ys.append(y)
        cs.append(c)
    EPS = 10 ** (-10)

    def isLE(a, b):
        return not a > b + EPS

    def getIntersectionLCs(a, b, c, xC, yC, r):
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
            (ae, be) = (a * e, b * e)
            (av, bv) = (a * v, b * v)
            xP1 = xC + (-ae + bv) / ab2
            yP1 = yC + (-be - av) / ab2
            xP2 = xC + (-ae - bv) / ab2
            yP2 = yC + (-be + av) / ab2
            return [(xP1, yP1), (xP2, yP2)]

    def getIntersectionCCs(x1, y1, r1, x2, y2, r2):
        (xC, yC) = (x2 - x1, y2 - y1)
        c = -(xC ** 2 + yC ** 2 + r1 ** 2 - r2 ** 2) / 2
        intCCs = getIntersectionLCs(xC, yC, c, 0, 0, r1)
        intCCs = [(x1 + x, y1 + y) for (x, y) in intCCs]
        return intCCs

    def countNum(xP, yP, xs, ys, rs, K):
        num = 0
        for (i, (x, y, r)) in enumerate(zip(xs, ys, rs), start=1):
            dist = hypot(x - xP, y - yP)
            if isLE(dist, r):
                num += 1
            if num >= K:
                return True
            elif num + N - i < K:
                return False
        return num >= K

    def isOK(t):
        rs = [t / c for c in cs]
        for (xP, yP) in zip(xs, ys):
            if countNum(xP, yP, xs, ys, rs, K):
                return True
        for i in range(N):
            (x1, y1, r1) = (xs[i], ys[i], rs[i])
            for j in range(i + 1, N):
                (x2, y2, r2) = (xs[j], ys[j], rs[j])
                intCCs = getIntersectionCCs(x1, y1, r1, x2, y2, r2)
                for (xP, yP) in intCCs:
                    if countNum(xP, yP, xs, ys, rs, K):
                        return True
        return False
    (ng, ok) = (0, 2 * 10 ** 5)
    while abs(ok - ng) > 10 ** (-7):
        mid = (ng + ok) / 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


solve()
