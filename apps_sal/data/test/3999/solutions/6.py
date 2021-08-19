from collections import defaultdict
(N,) = map(int, input().split())
dd = defaultdict(int)
cc = dict()
nrm = dict()
ss = []
for _ in range(N):
    xs = list(map(int, input().split()))
    cnd = [tuple(xs[j:] + xs[:j]) for j in range(4)]
    x = min(cnd)
    for item in cnd:
        nrm[item] = x
    dd[x] += 1
    cc[x] = (4 if x[0] == x[1] else 2) if x[0] == x[2] and x[1] == x[3] else 1
    ss.append(x)


def f(ff, gg):
    (a, b, c, d) = ff
    (e, h, g, f) = gg
    tl = [(a, e, f, b), (b, f, g, c), (c, g, h, d), (d, h, e, a)]
    q = defaultdict(int)
    for p in tl:
        if p not in nrm:
            return 0
        q[nrm[p]] += 1
    r = 1
    for (p, c) in q.items():
        for i in range(c):
            r *= dd[p] - i
        r *= cc[p] ** c
    return r


r = 0
for i in range(N):
    ff = ss[i]
    dd[ff] -= 1
    for j in range(i + 1, N):
        sl = ss[j]
        (x, y, z, w) = sl
        dd[sl] -= 1
        r += sum((f(ff, tuple(sl[j:] + sl[:j])) for j in range(4)))
        dd[sl] += 1
print(r)
