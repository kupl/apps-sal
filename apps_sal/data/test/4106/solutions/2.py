N, K, X = list(map(int, input().split()))
arr = [0] + [int(i) for i in input().split()]

dp = [[float('-inf') for _ in range(X + 1)] for _ in range(N + 1)]
dp[0][X] = 0

for i in range(1, N + 1):
    for x in range(X):
        for p in range(1, K + 1):
            if i - p < 0:
                break
            if dp[i - p][x + 1] < 0:
                continue
            dp[i][x] = max(dp[i][x], dp[i - p][x + 1] + arr[i])

ans = max([max(v) for v in dp[N - K + 1:]])

if ans < 0:
    print(-1)
else:
    print(ans)
