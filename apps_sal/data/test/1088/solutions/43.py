mo = 998244353
fact = [0] * 100
fact[0] = 1
for i in range(1, 100):
    fact[i] = fact[i - 1] * i % mo
(n, K) = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
fa = [i for i in range(n)]
fc = [1 for i in range(n)]


def getF(p, u):
    if p[p[u]] == p[u]:
        return p[u]
    p[u] = getF(p, p[u])
    return p[u]


def uniF(p, c, u, v):
    u = getF(p, u)
    v = getF(p, v)
    if u == v:
        return
    p[u] = v
    c[v] += c[u]


for i in range(n):
    for j in range(n):
        f = True
        for k in range(n):
            if a[i][k] + a[j][k] > K:
                f = False
                break
        if f:
            uniF(fa, fc, i, j)
fb = [i for i in range(n)]
fd = [1 for i in range(n)]
for i in range(n):
    for j in range(n):
        f = True
        for k in range(n):
            if a[k][i] + a[k][j] > K:
                f = False
                break
        if f:
            uniF(fb, fd, i, j)
ans = 1
for i in range(n):
    if getF(fa, i) == i:
        ans = ans * fact[fc[i]] % mo
    if getF(fb, i) == i:
        ans = ans * fact[fd[i]] % mo
print(ans)
