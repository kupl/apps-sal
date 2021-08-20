(a, b, c) = map(int, input().split())
MOD = 998244353
(A, B, C) = (a * (a + 1) // 2, b * (b + 1) // 2, c * (c + 1) // 2)
print(A * B * C % MOD)
