import math


def intersectionCC0(x1, y1, r1, r2):
    r = x1 ** 2 + y1 ** 2
    t = (r + r1 ** 2 - r2 ** 2) / (2 * r)
    dd = r1 ** 2 / r - t ** 2
    if -10 ** (-8) < dd < 0:
        dd = 0
    if dd < 0:
        return []
    (x, y) = (t * x1, t * y1)
    if dd == 0:
        return [(x, y)]
    sq = math.sqrt(dd)
    (dx, dy) = (y1 * sq, -x1 * sq)
    return [(x + dx, y + dy), (x - dx, y - dy)]


def intersectionCC(x1, y1, x2, y2, r1, r2):
    return [(x1 + x, y1 + y) for (x, y) in intersectionCC0(x2 - x1, y2 - y1, r1, r2)]


def chk(t):
    L = [a for a in L0]
    for (i, (x1, y1, c1)) in enumerate(X):
        for (x2, y2, c2) in X[:i]:
            L += intersectionCC(x1, y1, x2, y2, t / c1, t / c2)
    for (x0, y0) in L:
        cnt = 0
        for (x, y, c) in X:
            if math.sqrt((x - x0) ** 2 + (y - y0) ** 2) * c <= t + 10 ** (-8):
                cnt += 1
        if cnt >= K:
            return 1
    return 0


(N, K) = map(int, input().split())
X = []
L0 = []
for _ in range(N):
    (x, y, c) = map(int, input().split())
    X.append((x, y, c))
    L0.append((x, y))
(l, r) = (0, 150000)
while (r - l) * (1 << 20) > max(1, l):
    m = (l + r) / 2
    if chk(m):
        r = m
    else:
        l = m
print((l + r) / 2)
