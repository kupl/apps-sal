(A, B, C) = map(int, input().split())
D = A * (A + 1) * B * (B + 1) * C * (C + 1) // 8
print(D % 998244353)
