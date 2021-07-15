N = int(input())
dp = [i for i in range(N + 1)]

for i in range(N + 1):
    index = 1
    while 6 ** index <= i:
        dp[i] = min(dp[i], dp[i - (6 ** index)] + 1)
        index += 1

    index = 1
    while 9 ** index <= i:
        dp[i] = min(dp[i], dp[i - (9 ** index)] + 1)
        index += 1

print(dp[N])
