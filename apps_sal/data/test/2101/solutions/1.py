r, g, b = map(int, input().split())
red = list(map(int, input().split()))
green = list(map(int, input().split()))
blue = list(map(int, input().split()))
red.sort()
green.sort()
blue.sort()
red = red[::-1]
green = green[::-1]
blue = blue[::-1]

dp = []
for i in range(r + 1):
    temp = [[0] * (b + 1) for j in range(g + 1)]
    dp.append(temp)

answer = 0

for i in range(0, r + 1):
    for j in range(0, g + 1):
        for k in range(0, b + 1):
            if i > 0 and j > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k] + red[i - 1] * green[j - 1])
            if i > 0 and k > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1] + red[i - 1] * blue[k - 1])
            if j > 0 and k > 0:
                dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k - 1] + green[j - 1] * blue[k - 1])

            answer = max(answer, dp[i][j][k])
print(answer)
