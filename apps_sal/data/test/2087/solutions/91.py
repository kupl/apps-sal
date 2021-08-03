A, B, C = map(int, input().split())
sum = A * (A + 1) // 2 * B * (B + 1) // 2 * C * (C + 1) // 2
print(sum % 998244353)
