h, w, n, *l = map(int, open(0).read().split())
g = [[] for i in range(h)]
r = t = 0
for i, c in enumerate(l):
    i += 1
    while c >= (s := w - t):
        g[r] += [i] * s
        r += 1; c -= s; t = 0
    if c:
        g[r] += [i] * c
        t += c
for i in range(h): print(*g[i][::2 * (i % 2) - 1])
