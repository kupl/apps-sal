N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[] for i in range(N)]
dp[0] = A[0] + B[0]
UpSum = A[0]
for i in range(1, N):
    UpSum += A[i]
    dp[i] = max(dp[i - 1], UpSum) + B[i]
print(dp[-1])
