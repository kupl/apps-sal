(n, m) = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
mod = 10 ** 9 + 7
SX = 0
for i in range(n):
    SX += i * X[i] - (n - 1 - i) * X[i]
SX %= mod
SY = 0
for i in range(m):
    SY += i * Y[i] - (m - 1 - i) * Y[i]
SY %= mod
ans = SX * SY
print(ans % mod)
