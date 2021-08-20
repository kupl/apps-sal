L = int(1000000000.0 + 7)
N = int(input())
dp = [0 for _ in range(N)]
dp[0] = 1
index = 0
for _ in range(N):
    s = input()
    if s == 'f':
        index += 1
    if s == 's':
        for i in range(1, index + 1):
            dp[i] = (dp[i - 1] + dp[i]) % L
print(dp[index])
