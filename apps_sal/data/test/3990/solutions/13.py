(n, m) = list(map(int, input().split()))
f = [set() for i in range(n)]
(g, h) = ([0] + (n - 1) * [10000], [0] + (n - 1) * [10000])
for i in range(m):
    (u, v) = list(map(int, input().split()))
    f[u - 1].add(v - 1)
    f[v - 1].add(u - 1)
p = {i for i in range(1, n)}


def findrailway(t):
    if t == 0:
        for c in f[t]:
            g[c] = g[t] + 1
        for c in f[t]:
            findrailway(c)
    if t != n - 1:
        pp = set()
        for c in f[t] - f[0]:
            if g[c] != min(g[c], g[t] + 1):
                g[c] = g[t] + 1
                pp.add(c)
        for c in pp:
            findrailway(c)


def findbusway(t):
    if t == 0:
        for c in p - f[t]:
            h[c] = h[t] + 1
        for c in p - f[t]:
            findbusway(c)
    if t != n - 1:
        pp = set()
        for c in p - f[t] - (p - f[0]):
            if h[c] != min(h[c], h[t] + 1):
                h[c] = h[t] + 1
                pp.add(c)
        for c in pp:
            findbusway(c)


findrailway(0)
findbusway(0)
print(max(h[n - 1], g[n - 1]) if h[n - 1] != g[n - 1] and h[n - 1] < 10000 and (g[n - 1] < 10000) else -1)
