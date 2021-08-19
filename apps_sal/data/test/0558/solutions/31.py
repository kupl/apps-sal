(n, m, k) = map(int, input().split())
mod = 998244353
ans = 0
fact = [1] * (n + 1)
factinv = [1] * (n + 1)
for i in range(n):
    fact[i + 1] = fact[i] * (i + 1) % mod
    factinv[i + 1] = pow(fact[i + 1], mod - 2, mod)


def nCk(n, k):
    return fact[n] * factinv[n - k] * factinv[k] % mod


for k_i in range(k + 1):
    ans += m * pow(m - 1, n - 1 - k_i, mod) * nCk(n - 1, k_i)
    ans %= mod
print(ans)
