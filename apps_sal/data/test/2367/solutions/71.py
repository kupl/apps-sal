H, W, A, B = map(int, open(0).read().split())
MOD = 10**9 + 7


def modcomb(m, n, mod):
    if n > m - n:
        n = m - n
    p = 1
    q = 1
    for i in range(n):
        p = p * (m - i) % mod
        q = q * (i + 1) % mod
    result = p * pow(q, mod - 2, mod) % mod
    return result


total = modcomb(H + W - 2, W - 1, MOD)

tmp = modcomb(A + W - 2, W - 1, MOD)
total -= tmp

for i in range(B - 1):
    a = H - A + i
    b = i + 1
    c = W - i - 1
    d = W + A - 2 - i
    tmp = tmp * a * c % MOD
    tmp = tmp * pow(b, -1, MOD) % MOD
    tmp = tmp * pow(d, -1, MOD) % MOD
    total = (total - tmp) % MOD

print(total)
