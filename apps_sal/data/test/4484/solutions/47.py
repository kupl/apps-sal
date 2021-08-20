import math
(N, M) = map(int, input().split())


def mod(num):
    return num % (10 ** 9 + 7)


def calc():
    dp[1] = 1
    for i in range(2, maxmn + 1):
        dp[i] = mod(dp[i - 1] * i)


absnm = abs(N - M)
maxmn = max(N, M)
dp = [0] * (maxmn + 1)
if absnm > 1:
    print(0)
else:
    calc()
    if absnm == 1:
        r = mod(dp[M] * dp[N])
    elif absnm == 0:
        r = mod(dp[M] * dp[N] * 2)
    else:
        r = 0
    print(r)
