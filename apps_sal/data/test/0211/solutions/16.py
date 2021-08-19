MOD = 1000000009
(n, m, k) = map(int, input().split())
x = max(0, m - (n - n % k) // k * (k - 1) - n % k)
res = (pow(2, x + 1, MOD) - 2) % MOD * k % MOD
z = (m - x * k) % MOD
res = (res + z) % MOD
print(res)
