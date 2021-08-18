rev = {'B': 'W', 'W': 'B'}

n, k = list(map(int, input().split()))
a = list(input())

if all([a[0] == x for x in a]):
    print(''.join(a))
    return

f = [i for i in range(n)]
c = [1 for i in range(n)]


def getF(u):
    if f[u] == u:
        return u
    if f[f[u]] == f[u]:
        return f[u]
    f[u] = getF(f[u])
    return f[u]


def uniF(u, v):
    u, v = list(map(getF, (u, v)))
    if u == v:
        return
    f[u] = v
    c[v] += c[u]


for i in range(n):
    if a[i] == a[(i - 1) % n]:
        uniF(i, (i - 1) % n)
    if a[i] == a[(i + 1) % n]:
        uniF(i, (i + 1) % n)

p = []

for i in range(n):
    if getF(i) == i and c[i] > 1:
        p.append(i)

if len(p) == 0:
    if k % 2:
        a = list(map(rev.__getitem__, a))
    print(''.join(a))
    return

for i in range(len(p)):
    u = p[i]
    while a[(u + 1) % n] == a[p[i]]:
        u = (u + 1) % n
    v = p[(i + 1) % len(p)]
    while a[(v - 1) % n] == a[p[(i + 1) % len(p)]]:
        v = (v - 1) % n
    if v < u:
        v += n
    l = v - u - 1
    if 2 * k >= l:
        for i in range(u, u + l // 2 + 1):
            a[i % n] = a[u]
        for i in range(u + l // 2 + 1, v):
            a[i % n] = a[v % n]
    else:
        for i in range(u + 1, u + k + 1):
            a[i % n] = a[u]
        for i in range(v - k, v):
            a[i % n] = a[v % n]
        for i in range(u + k + 1, v - k):
            a[i % n] = rev[a[(i - 1) % n]]

print(''.join(a))
