n, m = map(int, input().split())

ab = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * m

for i in range(n):
    for j in range(ab[i][0]):
        k = ab[i][j + 1]
        dp[k - 1] += 1

print(dp.count(n))
