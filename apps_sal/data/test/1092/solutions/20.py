x, y = map(int, input().split())
fa = [0] * (x + 1)
fa[0] = 1
md = (10**9) + 7
for n in range(1, x + 1):
    fa[n] = (fa[n - 1] * n) % md


def bnp(bs, pw):
    res = 1
    while pw:
        if pw & 1:
            res *= bs
            res %= md
        bs *= bs
        bs %= md
        pw //= 2

    return res


s = sorted(list(map(int, input().split())))

res = fa[x - y]
res *= bnp(fa[s[0] - 1], md - 2)
res %= md
for n in range(1, y):
    v = s[n] - s[n - 1] - 1
    if v:
        res *= bnp(fa[v], md - 2)
        res %= md

u = x - s[-1]
if u:
    res *= bnp(fa[u], md - 2)
    res %= md

for n in range(1, y):
    u = s[n] - s[n - 1] - 1
    if u:
        res *= bnp(2, u - 1)
        res %= md

print(res % md)
