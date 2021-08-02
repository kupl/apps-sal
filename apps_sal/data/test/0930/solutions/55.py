n, k = list(map(int, input().split()))
mod = 10**9 + 7


def inv(x):
    return pow(x, mod - 2, mod)


N = 2 * 10**5
Fact = [0 for i in range(N + 1)]
Finv = [0 for i in range(N + 1)]
Fact[0] = 1
for i in range(N):
    Fact[i + 1] = (Fact[i] * (i + 1)) % mod
Finv[N] = inv(Fact[N])
for i in range(N - 1, -1, -1):
    Finv[i] = ((i + 1) * Finv[i + 1]) % mod


def C(a, b):
    return (Fact[a] * (Finv[b] * Finv[a - b]) % mod) % mod


ans = 0
for i in range(min(n, k + 1)):
    ans += (C(n, i) * C(n - 1, i)) % mod
    ans %= mod
print(ans)
