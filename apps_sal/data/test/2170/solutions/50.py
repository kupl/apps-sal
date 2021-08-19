MOD = 10 ** 9 + 7
MAX = 5 * 10 ** 5 + 1
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


(n, m) = map(int, input().split(' '))
ans = 0
for k in range(n + 1):
    tmp = nCk(n, k) * nPk(m, k) * nPk(m - k, n - k) * nPk(m - k, n - k) % MOD
    if not k % 2:
        ans += tmp
    else:
        ans -= tmp
    ans %= MOD
print(ans)
