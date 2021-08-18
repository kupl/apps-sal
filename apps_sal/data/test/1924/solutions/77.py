def inpl():
    return list(map(int, input().split()))


def cmb(n, r):
    if n < r:
        return 0
    r = min(n - r, r)
    if r == 0:
        return 1
    return (over[n] * under[r] * under[n - r]) % MOD


def extGCD(x, y):
    r = [1, 0, x]
    w = [0, 1, y]
    while w[2] != 1:
        q = r[2] // w[2]
        w_tmp = [r[0] - q * w[0], r[1] - q * w[1], r[2] % w[2]]
        r, w = w, w_tmp

    return w[:2]


def mod_inv(a, m):
    _, x = extGCD(m, a)
    return (x + m) % m


def g(x, y):
    return (cmb(x + y + 2, x + 1) - 1 + MOD) % MOD


r1, c1, r2, c2 = inpl()

MOD = 10**9 + 7

over = [0 for i in range(r2 + c2 + 3)]
under = [0 for i in range(r2 + c2 + 3)]
over[0] = 1
for i in range(r2 + c2 + 2):
    over[i + 1] = over[i] * (i + 1) % MOD

under[r2 + c2 + 2] = mod_inv(over[r2 + c2 + 2], MOD)
for i in range(r2 + c2 + 1, 0, -1):
    under[i] = under[i + 1] * (i + 1) % MOD

print(((g(r2, c2) - g(r2, c1 - 1) - g(r1 - 1, c2) + g(r1 - 1, c1 - 1)) % MOD))
