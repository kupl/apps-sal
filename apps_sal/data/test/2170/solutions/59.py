n, m = list(map(int, input().split()))

N = m + 100
MOD = 10 ** 9 + 7
fact = [0 for _ in range(N)]
invfact = [0 for _ in range(N)]
fact[0] = 1
for i in range(1, N):
    fact[i] = i * fact[i - 1] % MOD

invfact[N - 1] = pow(fact[N - 1], MOD - 2, MOD)

for i in range(N - 2, -1, -1):
    invfact[i] = invfact[i + 1] * (i + 1) % MOD


def nCk(n, k):
    if k < 0 or n < k:
        return 0
    else:
        return fact[n] * invfact[k] * invfact[n - k] % MOD


def nPk(n, k):
    return fact[n] * invfact[n - k] % MOD


ans = 0
sign = 1

for i in range(n + 1):
    ans = (ans + nPk(m, i) * nCk(n, i) * nPk(m - i, n - i) ** 2 * sign) % MOD
    sign *= -1

print(ans)
