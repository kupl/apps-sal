from bisect import bisect_left, bisect_right
N = int(input())
time = list(map(int, input().split()))
vel = list(map(int, input().split()))
sum_t = [0 for i in range(N + 1)]
for i in range(1, N + 1):
    sum_t[i] = sum_t[i - 1] + time[i - 1]
dp = [[-float('inf') for j in range(101)] for i in range(20001)]
dp[0][0] = 0
for i in range(1, sum_t[-1] + 1):
    bef = bisect_left(sum_t, i - 1)
    phase = bisect_left(sum_t, i)
    bef_bound = vel[bef - 1]
    bound = vel[phase - 1]
    if bef == 0:
        bef_bound = 100
    if bef_bound < bound:
        for j in range(bef_bound + 2):
            if j == 0:
                if j + 1 <= bef_bound:
                    dp[i][j] = max(dp[i - 1][j] + j + 0.25, dp[i - 1][j + 1] + j + 0.5)
                elif j == bef_bound:
                    dp[i][j] = dp[i - 1][j] + j + 0.25
            elif j >= 1:
                if j + 1 <= bef_bound:
                    dp[i][j] = max(dp[i - 1][j - 1] + j - 0.5, dp[i - 1][j] + j + 0.25, dp[i - 1][j + 1] + j + 0.5)
                elif j == bef_bound:
                    dp[i][j] = max(dp[i - 1][j - 1] + j - 0.5, dp[i - 1][j] + j + 0.25)
                elif j - 1 == bef_bound:
                    dp[i][j] = dp[i - 1][j - 1] + j - 0.5
    elif bef_bound >= bound:
        for j in range(bound):
            if j == 0:
                dp[i][j] = max(dp[i - 1][j] + j + 0.25, dp[i - 1][j + 1] + j + 0.5)
            elif j >= 1:
                dp[i][j] = max(dp[i - 1][j - 1] + j - 0.5, dp[i - 1][j] + j + 0.25, dp[i - 1][j + 1] + j + 0.5)
        dp[i][bound] = max(dp[i - 1][bound] + bound, dp[i - 1][bound - 1] + bound - 0.5)
ans = dp[sum_t[-1]][0]
print(ans)
