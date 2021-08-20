(N, X, Y) = map(int, input().split())
dp = [[0] * N for i in range(N)]
dist = [0] * N
X -= 1
Y -= 1
for i in range(N):
    for j in range(N):
        if not i < j:
            continue
        dp[i][j] = min(j - i, abs(j - Y) + 1 + abs(X - i))
        dist[dp[i][j]] += 1
for i in dist[1:]:
    print(i)
