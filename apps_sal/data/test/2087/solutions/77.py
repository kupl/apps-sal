(A, B, C) = map(int, input().split())
MOD = 998244353
a = A * (A + 1) // 2
b = B * (B + 1) // 2
c = C * (C + 1) // 2
ans = a * b % MOD * c % MOD
print(ans)
