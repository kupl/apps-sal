import sys
readline = sys.stdin.readline
(N, K) = map(int, readline().split())
A = list((int(x) for x in readline().split()))
bits = [0] * 50
for i in range(N):
    for j in range(50):
        if A[i] >> j & 1:
            bits[j] += 1
dp = [[0] * 2 for _ in range(50)]
for i in range(49)[::-1]:
    check_bit = 1 << i
    if K & check_bit:
        dp[i][1] = dp[i + 1][0] + bits[i] * check_bit
        if dp[i + 1][1] != 0:
            dp[i][1] = max(dp[i][1], dp[i + 1][1] + max(N - bits[i], bits[i]) * check_bit)
        dp[i][0] = dp[i + 1][0] + (N - bits[i]) * check_bit
    else:
        if dp[i + 1][1] != 0:
            dp[i][1] = dp[i + 1][1] + max(N - bits[i], bits[i]) * check_bit
        dp[i][0] = dp[i + 1][0] + bits[i] * check_bit
print(max(dp[0][0], dp[0][1]))
