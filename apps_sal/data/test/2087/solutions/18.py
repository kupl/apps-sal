A, B, C = map(int, input().split())
print((A * B * C * (A + 1) * (B + 1) * (C + 1) // 8) % 998244353)
