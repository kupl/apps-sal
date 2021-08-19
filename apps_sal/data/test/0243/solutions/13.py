(n, m, k) = map(int, input().split())
a = list(map(int, input().split()))
g = []
f = list(range(n + 1))
s = [0] * (n + 1)


def search(n):
    while f[n] != n:
        f[n] = f[f[n]]
        n = f[n]
    return n


def can_merge(u, v):
    u = search(u)
    v = search(v)
    f[u] = v
    if u == v:
        return False
    r = s[u] > 0 and s[v] > 0
    s[v] += s[u]
    return r


for _ in range(m):
    (u, v, w) = map(int, input().split())
    g.append((u, v, w))
g.sort(key=lambda tup: tup[2])
for i in a:
    s[i] += 1
ans = 0
for t in g:
    if can_merge(t[0], t[1]):
        ans = t[2]
print(' '.join([str(ans)] * k))
