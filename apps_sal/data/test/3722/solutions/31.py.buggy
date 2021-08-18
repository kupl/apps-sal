n = int(input())
aa = input()
ab = input()
ba = input()
bb = input()
MOD = 10 ** 9 + 7

if n == 2:
    print(1)
    return

if ab == "A":
    if aa == "A":
        print(1)
        return
    else:
        if ba == "A":
            dp = [[0] * 2 for _ in range(n + 1)]
            dp[0][0] = 1
            for i in range(n):
                dp[i + 1][0] = (dp[i][0] + dp[i][1]) % MOD
                dp[i + 1][1] = (dp[i][0]) % MOD
            print((dp[n - 3][0] + dp[n - 3][1]) % MOD)
            return
        else:
            ans = pow(2, n - 3, MOD)
            print(ans)
            return
else:
    if bb == "B":
        print(1)
        return
    else:
        if ba == "B":
            dp = [[0] * 2 for _ in range(n + 1)]
            dp[0][0] = 1
            for i in range(n):
                dp[i + 1][0] = (dp[i][0] + dp[i][1]) % MOD
                dp[i + 1][1] = (dp[i][0]) % MOD
            print((dp[n - 3][0] + dp[n - 3][1]) % MOD)
            return
        else:
            ans = pow(2, n - 3, MOD)
            print(ans)
            return
