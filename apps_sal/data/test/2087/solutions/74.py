A, B, C = map(int, input().split())
MOD = 998244353

c = C * (C + 1) // 2
b = B * (B + 1) // 2
a = A * (A + 1) // 2

print(a * b * c % MOD)
