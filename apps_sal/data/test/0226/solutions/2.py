N = int(input())
A = list(map(int, input().split()))

s = [0] * (N + 1)
dp = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    dp[i] = max(A[i] + s[i + 1] - dp[i + 1], dp[i + 1])
    s[i] = s[i + 1] + A[i]
print(s[0] - dp[0], dp[0])
