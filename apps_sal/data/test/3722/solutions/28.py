MOD = 10**9 + 7

def main():
    n = int(input())
    c = {}
    c["AA"] = input()
    c["AB"] = input()
    c["BA"] = input()
    c["BB"] = input()
    if n <= 3:
        print(1)
    else:
        if c["AB"] == "A":
            if c["AA"] == "A":
                print(1)
            else:
                if c["BA"] == "A":
                    dp = [[0]*2 for _ in range(n-2)]
                    dp[0][0] = 1
                    for i in range(1, n-2):
                        dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
                        dp[i][1] = dp[i-1][0]
                    print((dp[-1][0] + dp[-1][1])%MOD)
                else:
                    print(pow(2, n-3, MOD))
        else:
            if c["BB"] == "B":
                print(1)
            else:
                if c["BA"] == "B":
                    dp = [[0]*2 for _ in range(n-2)]
                    dp[0][0] = 1
                    for i in range(1, n-2):
                        dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % MOD
                        dp[i][1] = dp[i-1][0]
                    print((dp[-1][0] + dp[-1][1])%MOD)
                else:
                    print(pow(2, n-3, MOD))

def __starting_point():
    main()
__starting_point()
