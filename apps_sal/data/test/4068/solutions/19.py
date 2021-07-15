n, m = list(map(int, input().split()))
a = [int(input()) for _ in range(m)]
dp = [0] * n
for i in a:
    dp[i-1] = -1
if n == 1:
    if dp[0] == 0:
        print((1))
        return
    elif dp[0] == -1:
        print((0))
        return
if dp[1] >= 0 and dp[0] >= 0:
    dp[0] = 1
    dp[1] = 2
elif dp[1] == -1 and dp[0] >= 0:
    dp[0] = 1
elif dp[1] >= 0 and dp[0] == -1:
    dp[1] = 1
else:
    print((0))
    return
for j in range(2, n):
    if dp[j] >= 0:
        if dp[j-1] >= 0 and dp[j-2] >= 0:
            dp[j] = dp[j-1] + dp[j-2]
        elif dp[j-1] == -1 and dp[j-2] >= 0:
            dp[j] = dp[j-2]
        elif dp[j-1] >= 0 and dp[j-2] == -1:
            dp[j] = dp[j-1]
        else:
            print((0))
            return
print((dp[n-1] % (10**9+7)))

