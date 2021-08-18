MOD = 10**9 + 7
MAX = 10**5 + 1

fact = [0 for _ in range(MAX)]
factinv = [0 for _ in range(MAX)]

fact[0] = 1
for k in range(1, MAX):
    fact[k] = fact[k - 1] * k
    fact[k] %= MOD

factinv[MAX - 1] = pow(fact[MAX - 1], MOD - 2, MOD)
for k in range(MAX - 1, 0, -1):
    factinv[k - 1] = factinv[k] * k
    factinv[k - 1] %= MOD


def nCk(n, k):
    return fact[n] * factinv[k] * factinv[n - k] % MOD


def nPk(n, k):
    return fact[n] * factinv[n - k] % MOD


S = int(input())
ans = 0
for n in range(1, S):
    if 3 * n > S:
        break
    ans += nCk(S - 3 * n + n - 1, n - 1)
    ans %= MOD

print(ans)
