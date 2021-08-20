(n, m) = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
DX = [X[i + 1] - X[i] for i in range(n - 1)]
DY = [Y[i + 1] - Y[i] for i in range(m - 1)]
mod = 10 ** 9 + 7
SUM_X = 0
SUM_Y = 0
for i in range(n - 1):
    SUM_X += (i + 1) * (n - 1 - i) * DX[i]
    SUM_X %= mod
for i in range(m - 1):
    SUM_Y += (i + 1) * (m - 1 - i) * DY[i]
    SUM_Y %= mod
ans = SUM_X * SUM_Y % mod
print(ans)
