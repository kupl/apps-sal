n, m, k = list(map(int, input().split()))

mod = 10 ** 9 + 7
MAX = n * m

fact = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    fact[i] = (fact[i-1] * i) % mod

inv = [1] * (MAX + 1)
inv[MAX] = pow(fact[MAX], mod - 2, mod)
for i in range(MAX, 0, -1):
    inv[i-1] = (inv[i] * i) % mod


def comb(n, k):
    return fact[n] * inv[n-k] * inv[k] % mod


ans = 0
for i in range(n):
    for j in range(m):
        add = (n - i) * (m - j) * (i + j) % mod
        if i != 0 and j != 0:
            add *= 2
            add %= mod

        ans += add
        ans %= mod

ans *= comb(MAX - 2, k - 2)
ans %= mod
print(ans)

