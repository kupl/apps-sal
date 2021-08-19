(N, A) = map(int, input().split())
X = list(map(int, input().split()))
Y = [x - A for x in X]
dp = {0: 1}
for y in Y:
    tmp = list(dp.items())
    for (k, v) in tmp:
        dp[k + y] = dp.get(k + y, 0) + v
print(dp[0] - 1)
