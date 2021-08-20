mod = 10 ** 9 + 7
(n, m, k) = map(int, input().split())
nm = n * m
fact = [1] * (nm - 1)
inv = [1] * (nm - 1)
inv_fact = [1] * (nm - 1)
for i in range(2, nm - 1):
    fact[i] = fact[i - 1] * i % mod
    inv[i] = -(mod // i) * inv[mod % i] % mod
    inv_fact[i] = inv_fact[i - 1] * inv[i] % mod
comb = fact[nm - 2] * inv_fact[k - 2] * inv_fact[nm - k] % mod
cost_x = (n - 1) * nm * (n + 1) // 6 * m % mod
cost_y = (m - 1) * nm * (m + 1) // 6 * n % mod
print(comb * (cost_x + cost_y) % mod)
