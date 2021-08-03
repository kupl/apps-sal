class Solution:
    def knightDialer(self, n: int) -> int:
        d = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        dp = [[1] * 10]
        dp += [[0] * 10 for i in range(n - 1)]
        for i in range(n - 1):
            for j in range(10):
                for k in d[j]:
                    dp[i + 1][k] = (dp[i + 1][k] + dp[i][j]) % 1000000007
        return sum(dp[-1]) % 1000000007
