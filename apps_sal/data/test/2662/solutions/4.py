from bisect import bisect_left, bisect_right
n = int(input())
INF = 1010101010
dp = [INF] * n
a = [int(input()) for _ in range(n)]
a.reverse()
for i in a:
    dp[bisect_right(dp, i)] = i
print(bisect_left(dp, INF))
