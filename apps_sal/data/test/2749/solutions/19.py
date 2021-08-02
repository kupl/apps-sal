h, w, n, *l = map(int, open(0).read().split())
g = [[] for i in range(h)]
r = t = 0
for i, c in enumerate(l):
    i += 1
    while c >= (s := w - t):
        if r % 2: g[r] += [i] * s
        else: g[r] = [i] * s + g[r]
        r += 1
        c -= s
        t = 0
    if c:
        if r % 2: g[r] += [i] * c
        else: g[r] = [i] * c + g[r]
        t += c
for r in g: print(*r)
