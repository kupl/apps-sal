(A, B, C) = map(int, input().split())
A = A * (A + 1) // 2 % 998244353
B = B * (B + 1) // 2 % 998244353
C = C * (C + 1) // 2 % 998244353
X = A * B % 998244353
X = X * C % 998244353
print(int(X))
