mod = 10 ** 9 + 7
n, k = map(int, input().split())
binomial = [1]
cum = 1
for i in range(1, n + 2):
    cum *= i
    cum = cum % mod
    binomial.append(cum)
inv = []
tmp = pow(cum, mod - 2, mod)
inv.append(tmp)
for j in range(n + 1, 0, -1):
    tmp = j * tmp % mod
    inv.append(tmp)
inv.reverse()

def comb(n, k):
    return binomial[n] * inv[n - k] % mod * inv[k] % mod if n >= k else 0
k = min(k, n - 1)
ans = 0
for m in range(k + 1):
        tmp = comb(n, m) * binomial[n - 1] * inv[n - 1 - m] * inv[m]
        ans += tmp % mod
ans %= mod
print(ans)
