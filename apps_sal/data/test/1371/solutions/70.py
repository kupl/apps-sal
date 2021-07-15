import sys

# D - Redistribution
S = int(input())

if S < 3:
  print(0)
elif S < 6:
  print(1)
else:
  dp = [0] * (S + 1)

  dp[3] = 1
  dp[4] = 1
  dp[5] = 1

  for i in range(6, S + 1):
    dp[i] = 1

    for j in range(i - 2):
      dp[i] += dp[j]

    dp[i] %= 10 ** 9 + 7

  print(dp[S])
