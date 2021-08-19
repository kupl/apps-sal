from collections import defaultdict
(N,) = list(map(int, input().split()))


def normal(xs):
    mnx = min(xs)
    xi = xs.index(mnx)
    if xs[(xi + 3) % 4] == mnx:
        if xs[(xi + 2) % 4] == mnx:
            xi = (xi + 2) % 4
        else:
            xi = (xi + 3) % 4
    if xs[(xi + 1) % 4] > xs[(xi + 3) % 4]:
        xi = (xi + 2) % 4
    return (xs[xi % 4], xs[(xi + 1) % 4], xs[(xi + 2) % 4], xs[(xi + 3) % 4])


dd = defaultdict(int)
cc = defaultdict(int)
ss = []
for _ in range(N):
    (a, b, c, d) = list(map(int, input().split()))
    x = normal([a, b, c, d])
    n = 1
    if x[0] == x[2] and x[1] == x[3]:
        n *= 2
        if x[0] == x[1]:
            n *= 2
    dd[x] += 1
    cc[x] = n
    ss.append(x)


def icr(x):
    dd[x] += 1


def dcr(x):
    dd[x] -= 1


def f(ff, gg):
    (a, b, c, d) = ff
    (e, h, g, f) = gg
    tl = list(map(normal, [(a, e, f, b), (b, f, g, c), (c, g, h, d), (d, h, e, a)]))
    r = 1
    for cp in tl:
        if cp not in dd:
            r = 0
            break
        r *= dd[cp] * cc[cp]
        dcr(cp)
    for cp in tl:
        if cp not in dd:
            break
        icr(cp)
    return r


r = 0
for i in range(N):
    ff = ss[i]
    dcr(ff)
    for j in range(i + 1, N):
        sl = ss[j]
        dcr(sl)
        (x, y, z, w) = sl
        sls = [(x, y, z, w), (y, z, w, x), (z, w, x, y), (w, x, y, z)]
        for s in sls:
            r += f(ff, s)
        icr(sl)
    icr(ff)
print(r // 3)
