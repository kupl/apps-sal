N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
dp = [[0, 0]for _ in range(42)]

for i in range(1, 42):
    if dp[i - 1][1] == 1:
        dp[i][1] = 1

    cnt = 0
    for j in range(N):
        if (A[j] >> (41 - i)) & 1 == 1:
            cnt += 1

    if cnt >= N - cnt:
        dp[i][0] = dp[i - 1][0] + (2**(41 - i)) * cnt
        if (K >> (41 - i)) & 1 == 1:
            dp[i][1] = 1
    else:
        if dp[i][1] == 1:
            dp[i][0] = dp[i - 1][0] + (2**(41 - i)) * (N - cnt)
        else:
            if (K >> (41 - i)) & 1 == 1:
                dp[i][0] = dp[i - 1][0] + (2**(41 - i)) * (N - cnt)
            else:
                dp[i][0] = dp[i - 1][0] + (2**(41 - i)) * cnt
print((dp[41][0]))
