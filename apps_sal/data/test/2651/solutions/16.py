N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
X, Y = X[::-1], Y[::-1]

MOD = 10**9 + 7
x_sum, y_sum = 0, 0

for i in range(N):
    x_sum = x_sum + (N - i - 1) * X[i]
X = X[::-1]
for i in range(N):
    x_sum = x_sum - (N - i - 1) * X[i]
x_sum %= MOD

for i in range(M):
    y_sum = y_sum + (M - i - 1) * Y[i]
Y = Y[::-1]
for i in range(M):
    y_sum = y_sum - (M - i - 1) * Y[i]
y_sum %= MOD

print((x_sum * y_sum) % MOD)
