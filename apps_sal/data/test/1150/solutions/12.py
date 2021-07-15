def r(t): t[0], t[1] = t[2] + t[3] - t[1], t[3] + t[0] - t[2]
f = [(0, 0), (1, 3), (2, 15), (3, 63)]
h = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
g = lambda u, v: (u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2
for i in range(int(input())):
    p = [list(map(int, input().split())) for j in range(4)]
    s = 13
    for q in range(256):
        t = sum((q >> k) & 3 for k in (0, 2, 4, 6))
        d = sorted(g(p[u], p[v]) for u, v in h)
        if 0 != d[4] == d[5] == 2 * d[0] == 2 * d[3]: s = min(s, t)
        for i, k in f:
            if q & k == k: r(p[i])
    print(s if s < 13 else -1)
