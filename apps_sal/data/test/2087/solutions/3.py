(A, B, C) = map(int, input().split())
s = A * (A + 1) // 2 * (B * (B + 1) // 2) * (C * (C + 1) // 2)
print(s % 998244353)
