n = int(input())

dp = [True] * (n * 1000000)
dp[n] = False
res = 1
while n < 1000001:
    res += 1
    if n % 2 == 1:
        n = n * 3 + 1
    else:
        n = n // 2

    if dp[n]:
        dp[n] = False
    else:
        print(res)
        return
