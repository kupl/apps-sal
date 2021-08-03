def r(t): t[0], t[1] = t[2] + t[3] - t[1], t[3] + t[0] - t[2]


f = range(4)
def g(u, v): return (u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2


h = [(i, j) for i in f for j in f if i < j]
for i in range(int(input())):
    p = [list(map(int, input().split())) for j in f]
    s = 13
    for a in f:
        for b in f:
            for c in f:
                for d in f:
                    t = sorted(g(p[u], p[v]) for u, v in h)
                    if 0 != t[4] == t[5] == 2 * t[0] == 2 * t[3]:
                        s = min(s, a + b + c + d)
                    r(p[3])
                r(p[2])
            r(p[1])
        r(p[0])
    print(s if s < 13 else -1)
