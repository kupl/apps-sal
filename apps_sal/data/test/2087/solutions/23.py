(a, b, c) = map(int, input().split())
mod = 998244353
ans = 1
ans *= a % mod
ans *= (a + 1) % mod
ans *= b % mod
ans *= (b + 1) % mod
ans *= c % mod
ans *= (c + 1) % mod
ans //= 8
ans %= mod
print(ans)
