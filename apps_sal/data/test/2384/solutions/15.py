n = int(input())
a = list(map(int, input().split()))
if n % 2 == 0 and n >= 4:
  dp = [[0, 0] for i in range(n)]
  dp[0][0] = a[0]
  dp[1][1] = a[1]
  dp[2][0] = a[0] + a[2]
  for i in range(3, n):
    dp[i][0] = dp[i - 2][0] + a[i]
    dp[i][1] = max(dp[i - 3][0], dp[i - 2][1]) + a[i]
  print(max(dp[n - 2][0], dp[n - 1][1]))
elif n % 2 != 0 and n >= 5:
  dp = [[0, 0, 0] for i in range(n)]
  dp[0][0] = a[0]
  dp[1][1] = a[1]
  dp[2][0] = a[0] + a[2]
  dp[2][2] = a[2]
  dp[3][1] = a[1] + a[3]
  dp[3][2] = a[0] + a[3]
  for i in range(3, n):
    dp[i][0] = dp[i - 2][0] + a[i]
    dp[i][1] = max(dp[i - 3][0], dp[i - 2][1]) + a[i]
    dp[i][2] = max(dp[i - 4][0], dp[i - 3][1], dp[i - 2][2]) + a[i]
  print(max(dp[n - 3][0], dp[n - 2][1], dp[n - 1][2]))
elif n == 2:
  print(max(a[0], a[1]))
else:
  print(max(a[0], a[1], a[2]))
