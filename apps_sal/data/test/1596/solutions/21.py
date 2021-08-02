from pprint import pprint
mod = int(1e9) + 7
s = input()
if 'm' in s or 'w' in s:
    print(0)
else:
    n = len(s)
    dp = [[0, 0] for i in range(n)]

    for i in range(1, n):
        dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % mod

        if s[i] in 'un':
            if s[i] == s[i - 1]:
                dp[i][1] = (1 + dp[i - 1][0]) % mod

    # pprint(dp)
    print((dp[-1][0] + dp[-1][1] + 1) % mod)
