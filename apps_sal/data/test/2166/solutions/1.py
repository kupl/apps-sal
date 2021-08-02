MOD = 10**9 + 7
n = int(input())

notUsed = set(range(1, n + 1))
chairs = set()
for i, a in enumerate(map(int, input().split()), 1):
    if a == -1:
        chairs.add(i)
    else:
        notUsed -= {a}
fixed = len(chairs & notUsed)

m = len(notUsed)
U = m
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


ans = fact[m]
for k in range(1, fixed + 1):
    ans += nCr(fixed, k) * fact[m - k] * (-1)**k
    ans %= MOD
print(ans)
