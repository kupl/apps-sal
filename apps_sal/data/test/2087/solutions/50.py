A, B, C = map(int, input().split())
 
ans = A * (A + 1) * B * (B + 1) * C * (C + 1) // 8
ans %= 998244353
 
print(ans)
