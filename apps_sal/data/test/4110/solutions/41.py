d, g = map(int, input().split())
dp = [0 for i in range(1001)]
dp[0] = 0
num = 0
for i in range(1, d + 1):
    p, c = map(int, input().split())
    for j in range(num, -1, -1):
        for k in range(1, p + 1):
            if k != p:
                dp[j + k] = max(dp[j + k], dp[j] + 100 * i * k)
            else:
                dp[j + k] = max(dp[j + k], dp[j] + 100 * i * k + c)
    num += p
for i in range(1001):
    if dp[i] >= g:
        print(i)
        break
