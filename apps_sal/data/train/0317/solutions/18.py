class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n + 1)] for i in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(i + 1):
                if(s[i - 1] == 'D'):
                    for k in range(j, i):
                        dp[i][j] += dp[i - 1][k]
                else:
                    for k in range(j):
                        dp[i][j] += dp[i - 1][k]
        # print(dp)
        return sum(dp[n][:]) % (pow(10, 9) + 7)
