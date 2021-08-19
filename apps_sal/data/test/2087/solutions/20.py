(A, B, C) = list(map(int, input().split()))
MOD = 998244353
ans = A * (1 + A) // 2 * (B * (1 + B) // 2) * (C * (1 + C) // 2) % MOD
print(ans)
