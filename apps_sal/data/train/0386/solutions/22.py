class Solution:

    def countVowelPermutation(self, n: int) -> int:
        dp = [[0 for i in range(5)] for j in range(n)]
        for i in range(5):
            dp[-1][i] = 1
        d = {0: [1], 1: [0, 2], 2: [0, 1, 3, 4], 3: [2, 4], 4: [0]}
        for i in range(n - 2, -1, -1):
            for j in range(5):
                c = 0
                for e in d[j]:
                    c += dp[i + 1][e]
                dp[i][j] = c
        return (dp[0][0] + dp[0][1] + dp[0][2] + dp[0][3] + dp[0][4]) % 1000000007
