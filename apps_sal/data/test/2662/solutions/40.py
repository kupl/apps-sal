import bisect
N = int(input())
dp = [-1] * N
cnt = 0
for _ in range(N):
    a = int(input())
    idx = bisect.bisect_left(dp, a)
    dp[idx - 1] = a
print(len(dp[bisect.bisect_left(dp, 0):]))
