def prepare(n, MOD):
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return (factorials, invs)


MOD = 10 ** 9 + 7
(f, inv) = prepare(10 ** 5 + 100, MOD)
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
p = 0
m = 0
for i in range(n):
    if n - i >= k:
        cn = n - i - 1
        ck = k - 1
        if cn >= ck:
            combi = f[cn] * inv[ck] % MOD * inv[cn - ck] % MOD
            if a[i] >= 0:
                p += a[i] * combi % MOD
            else:
                p += a[i] * combi % -MOD
            if p >= 0:
                p %= MOD
            else:
                p %= -MOD
    if i >= k - 1:
        cn = i
        ck = k - 1
        if cn >= ck:
            combi = f[cn] * inv[ck] % MOD * inv[cn - ck] % MOD
            if a[i] >= 0:
                m += a[i] * combi % MOD
            else:
                m += a[i] * combi % -MOD
            if m >= 0:
                m %= MOD
            else:
                m %= -MOD
print((p - m) % MOD)
