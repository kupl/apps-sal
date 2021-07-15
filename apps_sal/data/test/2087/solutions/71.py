MOD = 998244353
a, b, c = map(int, input().split())
print((a * (a + 1) // 2 * b * (b + 1) // 2 * c * (c + 1) // 2) % MOD)
