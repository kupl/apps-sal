(A, B, C) = list(map(int, input().split()))
MOD = 998244353
Sa = A * (A + 1) // 2
Sb = B * (B + 1) // 2
Sc = C * (C + 1) // 2
print(Sa * Sb * Sc % MOD)
