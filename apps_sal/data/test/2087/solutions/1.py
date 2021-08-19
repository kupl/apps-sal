(A, B, C) = list(map(int, input().split()))
D = A * (A + 1) // 2 * (B * (B + 1) // 2) * (C * (C + 1) // 2)
print(D % 998244353)
