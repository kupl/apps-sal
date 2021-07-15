N, M = map(int, input().split())
mod = 10 ** 9 + 7

def calc(n):
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= mod
        factorials.append(f)
    inv = pow(f, mod - 2, mod)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= mod
        invs[m - 1] = inv
    return factorials, invs

factorials, invs = calc(M)
mPn = (factorials[M] * invs[M - N]) % mod
ans = (mPn * mPn) % mod
for k in range(1, N + 1):
    v = pow(-1, k - 1) * factorials[N] * factorials[M - k] * invs[N - k] * invs[k] * invs[M - N] % mod
    ans -= v * mPn
print(ans % mod)
