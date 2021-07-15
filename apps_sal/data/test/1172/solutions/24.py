MOD = 10**9 + 7
def main():
    s = input()
    dp = [[0]*3 for _ in range(len(s)+1)]
# dp[idx][A, AB, ABC]
    tmp = 1
    for i in range(len(s)):
        c = s[i]
        if c == "A":
            dp[i][0] += tmp
            dp[i][0] %= MOD
        elif c == "B":
            dp[i][1] += dp[i][0]
            dp[i][1] %= MOD
        elif c == "C":
            dp[i][2] += dp[i][1]
            dp[i][2] %= MOD
        else:
            pre = [v for v in dp[i]]
            dp[i] = [0, 0, 0]
# ? = A
            dp[i][0] += pre[0] + tmp
            dp[i][1] += pre[1]
            dp[i][2] += pre[2]
# ? = B
            dp[i][0] += pre[0]
            dp[i][1] += pre[0] + pre[1]
            dp[i][2] += pre[2]
# ? = C
            dp[i][0] += pre[0]
            dp[i][1] += pre[1]
            dp[i][2] += pre[1] + pre[2]
            tmp *= 3
            tmp %= MOD
            dp[i][0] %= MOD
            dp[i][1] %= MOD
            dp[i][2] %= MOD
        dp[i+1][0] = dp[i][0]
        dp[i+1][1] = dp[i][1]
        dp[i+1][2] = dp[i][2]
#        print(dp[i])
    print(dp[len(s)][2] % MOD)

def __starting_point():
    main()
__starting_point()
