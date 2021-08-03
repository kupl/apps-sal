N = 100001
a = [0] * N
input()
for i in map(int, input().split(' ')):
    a[i] += i
dp = [0] * N
for i in range(1, N):
    if i == 1:
        dp[i] = a[i]
    else:
        dp[i] = max(dp[i - 1], dp[i - 2] + a[i])
print(dp[N - 1])
