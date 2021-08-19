# 連続するK本のろうそくに火をつけるので、最小となる組を全探索する
N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = float("INF")
for i in range(N - K + 1):
    lr = abs(X[i]) + abs(X[i] - X[i + K - 1])
    rl = abs(X[i + K - 1]) + abs(X[i + K - 1] - X[i])
    ans = min(ans, min([lr, rl]))

print(ans)
