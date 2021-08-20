mod = 10 ** 9 + 7
(r1, c1, r2, c2) = map(int, input().split())


def inv(x):
    m = mod
    u = 1
    v = 0
    while m:
        t = x // m
        x -= t * m
        (x, m) = (m, x)
        u -= t * v
        (u, v) = (v, u)
    u %= mod
    if u < 0:
        u += mod
    return u


fac = [1]
for i in range(1, r2 + c2 + 3):
    fac.append(fac[i - 1] * i % mod)


def paths(r, c):
    return fac[r + c + 2] * inv(fac[r + 1] * fac[c + 1]) % mod


f = paths(r2, c2) - paths(r2, c1 - 1) - paths(r1 - 1, c2) + paths(r1 - 1, c1 - 1)
f %= mod
if f < 0:
    f += mod
print(f)
