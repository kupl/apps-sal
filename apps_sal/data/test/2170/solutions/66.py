MOD = 10 ** 9 + 7
(n, m) = list(map(int, input().split()))
U = max(n, m)
fact = [0] * (U + 1)
fact[0] = 1
for i in range(1, U + 1):
    fact[i] = fact[i - 1] * i % MOD
invfact = [0] * (U + 1)
invfact[U] = pow(fact[U], MOD - 2, MOD)
for i in reversed(list(range(U))):
    invfact[i] = invfact[i + 1] * (i + 1) % MOD


def nCr(n, r):
    if r < 0 or n < r:
        return 0
    return fact[n] * invfact[r] * invfact[n - r]


def nPr(n, r):
    return fact[n] * invfact[n - r]


ans = 0
for k in range(n + 1):
    tmp = nCr(n, k) * nPr(m, n) * nPr(m - k, n - k)
    if k % 2 == 0:
        ans += tmp
    else:
        ans -= tmp
    ans %= MOD
print(ans)
