input()
dp = [0] * 5
for (i, c) in zip(map('hard'.find, input()), map(int, input().split())):
    if i < 0:
        continue
    dp[i + 1] = min(dp[i + 1], dp[i])
    dp[i] += c
print(min(dp[:-1]))
