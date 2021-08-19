class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        mod = 10**9 + 7
        dp = [[0 for i in range(n + 1)] for j in range(10)]
        for i in range(10):
            dp[i][1] = 1
        d = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        for j in range(2, n + 1):
            for i in range(10):
                if i != 5:
                    for ele in d[i]:
                        dp[i][j] += dp[ele][j - 1]
                        dp[i][j] %= mod
        # print(dp)
        ans = 0
        for i in range(10):
            ans += dp[i][n]
            ans %= mod
        return ans
