(N, M) = map(int, input().split())
MOD = 10 ** 9 + 7
x = list(map(int, input().split()))
y = list(map(int, input().split()))
cumsum_x = [0] * N
cumsum_y = [0] * M
cumsum_x[0] = x[0]
cumsum_y[0] = y[0]
for (i, xi) in enumerate(x[1:], 1):
    cumsum_x[i] = (cumsum_x[i - 1] + xi) % MOD
for (i, yi) in enumerate(y[1:], 1):
    cumsum_y[i] = (cumsum_y[i - 1] + yi) % MOD
X = Y = 0
for (i, xi) in enumerate(x):
    X += (cumsum_x[-1] - cumsum_x[i] - (N - i - 1) * xi) % MOD
    X %= MOD
for (i, yi) in enumerate(y):
    Y += (cumsum_y[-1] - cumsum_y[i] - (M - i - 1) * yi) % MOD
    Y %= MOD
print(X * Y % MOD)
