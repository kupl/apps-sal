a, b, c = map(int, input().split())
mod = 998244353
C = c * (c + 1) // 2
B = b * (b + 1) // 2
A = a * (a + 1) // 2
print(int(A * B * C % mod))
