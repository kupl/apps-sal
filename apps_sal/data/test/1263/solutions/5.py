n, k = [int(x) for x in input().split(' ')]

taste = [int(x) for x in input().split(' ')]
cal = [int(x) for x in input().split(' ')]


d = [[0 for j in range(10000 * 2)] for i in range(n)]

a = taste
b = cal


w = [a[i] - k * b[i] for i in range(n)]

dp = [-9999999 for i in range(300005)]
dp[10000] = 0

for i in range(n):
    if w[i] > 0:
        for j in range(20000, w[i], -1):
            if dp[j - w[i]] != -9999999:
                dp[j] = max(dp[j], dp[j - w[i]] + a[i])
    else:
        for j in range(20000):
            if dp[j - w[i]] != -9999999:
                dp[j] = max(dp[j], dp[j - w[i]] + a[i])

if dp[10000] == 0:
    print(-1)
else:
    print(dp[10000])
