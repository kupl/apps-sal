(N, K) = list(map(int, input().split()))
A = list(map(int, input().split()))
M = 50
l = len(str(N))
dp = [[-1] * 2 for _ in range(M + 1)]
dp[0][0] = 0
for i in range(M):
    mask = 1 << M - i - 1
    num = 0
    for j in range(N):
        if A[j] & mask:
            num += 1
    c0 = mask * num
    c1 = mask * (N - num)
    if dp[i][1] != -1:
        dp[i + 1][1] = max(dp[i + 1][1], dp[i][1] + max(c0, c1))
    if dp[i][0] != -1:
        if K & mask:
            dp[i + 1][1] = max(dp[i + 1][1], dp[i][0] + c0)
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][0] + c1)
        else:
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][0] + c0)
print(max(dp[M][0], dp[M][1]))
