MOD = 1000000007

N, M = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

dx = [X[i + 1] - X[i] for i in range(N - 1)]
dy = [Y[i + 1] - Y[i] for i in range(M - 1)]

sx = 0
sy = 0

for i in range(N - 1):
    sx += dx[i] * (i + 1) * (N - 1 - i)
    sx %= MOD

for i in range(M - 1):
    sy += dy[i] * (i + 1) * (M - 1 - i)
    sy %= MOD

print(sx * sy % MOD)
