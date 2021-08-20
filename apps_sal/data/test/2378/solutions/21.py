from sys import setrecursionlimit
setrecursionlimit(2 * 10 ** 5)
n = int(input())
ab = [tuple([int(x) - 1 for x in input().split()]) for _ in range(n - 1)]
e = [[] for _ in range(n)]
for (a, b) in ab:
    e[a].append(b)
    e[b].append(a)
MOD = 10 ** 9 + 7
d = []


def modinv(x):
    a = x
    b = MOD
    u = 1
    v = 0
    while b:
        t = a // b
        a -= t * b
        (a, b) = (b, a)
        u -= t * v
        (u, v) = (v, u)
    u %= MOD
    if u < 0:
        u += MOD
    return u


def dfs(x, p):
    if len(e[x]) == 1:
        if e[x][0] == p:
            d.append(1)
            return 1
    ret = 1
    for z in e[x]:
        if z == p:
            continue
        ret += dfs(z, x)
    if x != 0:
        d.append(ret)
    return ret


dfs(0, -1)
f = []
w = 1
for i in range(n + 1):
    f.append(w)
    w = w * 2 % MOD
ans = 0
for x in d:
    ans += (f[x] - 1) * (f[n - x] - 1) % MOD
    ans %= MOD
ans = (ans - f[n - 1] * n + f[n] - 1 + MOD) % MOD
ans = ans * modinv(f[n]) % MOD
print(ans)
