from bisect import bisect_left
n = int(input())
a = [int(input()) for i in range(n)]
dp = [-float("inf")] * (n + 1)
for i in a:
    dp[bisect_left(dp, i) - 1] = i
print(dp[::-1].index(-float("inf")))
