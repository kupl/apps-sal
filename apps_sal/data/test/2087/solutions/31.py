a, b, c = list(map(int, input().split()))
mod = 998244353
ans = ((((a * (a + 1)) // 2) % mod) * (((b * (b + 1)) // 2) % mod) * (((c * (c + 1)) // 2) % mod)) % mod
print(ans)
