(A, B, C) = list(map(int, input().split()))
x = 998244353
ans = A * (A + 1) * B * (B + 1) * C * (C + 1) // 8
ans %= x
print(ans)
