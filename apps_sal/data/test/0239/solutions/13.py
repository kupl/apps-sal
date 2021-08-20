from math import sqrt
(n, m) = [int(s) for s in input().split()]
p = [(i, j) for i in range(4) for j in range(4) if i + j < 4 and i <= n and (j <= m)]
q = [(n - i, m - j) for (i, j) in p]
p = set(p + q)


def dist(a, b):
    return sqrt((a[0] - b[0]) ** 2.0 + (a[1] - b[1]) ** 2.0)


def dp(a, b, c, d):
    return dist(a, b) + dist(b, c) + dist(c, d)


t = -1
r = None
for a in p:
    for b in p:
        if b == a:
            continue
        for c in p:
            if c == a or c == b:
                continue
            for d in p:
                if d == a or d == b or d == c:
                    continue
                f = dp(a, b, c, d)
                if f > t:
                    r = (a, b, c, d)
                    t = f
for (i, j) in r:
    print(i, j)
