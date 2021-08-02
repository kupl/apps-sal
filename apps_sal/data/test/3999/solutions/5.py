from collections import defaultdict
N, = map(int, input().split())

dd = defaultdict(int)
cc = dict()
norm = dict()
ss = []
for _ in range(N):
    xs = list(map(int, input().split()))
    cnd = [tuple(xs[j:] + xs[:j]) for j in range(1, 5)]
    x = min(cnd)
    for item in cnd:
        norm[item] = x
    dd[x] += 1
    cc[x] = (4 if x[0] == x[1] else 2)if x[0] == x[2] and x[1] == x[3] else 1
    ss.append(x)


def f(ff, gg):
    a, b, c, d = ff
    e, h, g, f = gg
    tl = [(a, e, f, b), (b, f, g, c), (c, g, h, d), (d, h, e, a)]
    for i in range(4):
        if tl[i] not in norm:
            return 0
        tl[i] = norm[tl[i]]
    r = 1
    for cp in tl:
        r *= dd[cp] * cc[cp]
        dd[cp] -= 1
    for cp in tl:
        dd[cp] += 1
    return r


r = 0
for i in range(N):
    ff = ss[i]
    dd[ff] -= 1
    for j in range(i + 1, N):
        sl = ss[j]
        x, y, z, w = sl
        dd[sl] -= 1
        sls = [(x, y, z, w), (y, z, w, x), (z, w, x, y), (w, x, y, z)]
        for s in sls:
            r += f(ff, s)
        dd[sl] += 1
print(r)
