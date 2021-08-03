import sys

sys.setrecursionlimit(10**6)
stdin = sys.stdin


def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


n_ = 2 * 10**5 + 20
mod = 10**9 + 7
fun = [1] * (n_ + 1)
for i in range(1, n_ + 1):
    fun[i] = fun[i - 1] * i % mod
rev = [1] * (n_ + 1)
rev[n_] = pow(fun[n_], mod - 2, mod)
for i in range(n_ - 1, 0, -1):
    rev[i] = rev[i + 1] * (i + 1) % mod


def modinv(x, mod):
    x %= mod
    a, b = x, mod
    u, v = 1, 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    return u % mod


def nCr(n, r):
    if r > n:
        return 0
    return fun[n] * rev[r] % mod * rev[n - r] % mod


n = ni()
g = [list() for _ in range(n)]
for _ in range(n - 1):
    a, b = nm()
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

sl = [1] * n
pm = [1] * n


def dfs(v, p):
    for x in g[v]:
        if x == p:
            continue
        dfs(x, v)
        sl[v] += sl[x]
        pm[v] = pm[v] * pm[x] % mod
    sv = sl[v] - 1
    for x in g[v]:
        if x == p:
            continue
        pm[v] = pm[v] * nCr(sv, sl[x]) % mod
        sv -= sl[x]
    return


def dfs2(v, p):
    pp = pm[p] * modinv(nCr(n - 1, sl[v]) * pm[v], mod) % mod
    sp = n - sl[v]
    pm[v] = pm[v] * pp % mod * nCr(n - 1, sp) % mod
    for x in g[v]:
        if x == p:
            continue
        dfs2(x, v)


dfs(0, -1)
for x in g[0]:
    dfs2(x, 0)

print(*pm, sep='\n')
