n, m, k = map(int, input().split())
mod = 998244353
ans = 0
x = 1
for i in range(k + 1):
    ans += (((m * pow(m - 1, n - i - 1, mod)) % mod) * x) % mod
    ans %= mod
    x = (x * (n - i - 1) * pow(i + 1, mod - 2, mod)) % mod
print(ans % mod)
