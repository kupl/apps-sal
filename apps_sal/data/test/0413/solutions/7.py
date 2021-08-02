#import sys
# sys.setrecursionlimit(20000)
f = lambda: input()
n, m = list(map(int, f().split()))

dp = [99999] * 10001
dp[n] = 0


def click():
    for i in range(0, n + 1):
        dp[i] = n - i;
        if i * 2 <= 10000:
            if dp[i * 2] > dp[i] + 1:
                dp[i * 2] = dp[i] + 1

    for i in range(n + 1, 10001):
        if dp[i] == 99999:
            d = 1
            while(i + d <= 10000 and dp[i + d] == 99999):
                d += 1
            if i + d <= 10000:
                dp[i] = d + dp[i + d]

        if i * 2 <= 10000 and dp[i * 2] > dp[i] + 1:
            dp[i * 2] = dp[i] + 1


click()

# print(dp)
print(dp[m])
