(n, a) = map(int, input().split())
A = list(map(int, input().split()))
for i in range(n):
    A[i] = A[i] - a
B = []
c = 0
for i in range(n):
    if A[i] == 0:
        c = c + 1
    else:
        B.append(A[i])
n = len(B)
dp = [[0] * 5010 for i in range(n + 1)]
for i in range(1, n + 1):
    dp[i] = dp[i - 1][0:5010]
    dp[i][2505 + B[i - 1]] += 1
    for j in range(5010):
        if 0 <= j + B[i - 1] and j + B[i - 1] <= 5009:
            dp[i][j + B[i - 1]] += dp[i - 1][j]
ans = dp[n][2505]
print((ans + 1) * 2 ** c - 1)
