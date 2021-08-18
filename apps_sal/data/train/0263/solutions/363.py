class Solution:
    def knightDialer(self, n: int) -> int:
        stack = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 9], [4, 2]]
        dp = [[0 for _ in range(10)] for __ in range(n)]
        for i in range(10):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(10):
                for k in stack[j]:
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % (10**9 + 7)
        return sum(dp[-1][i] for i in range(10)) % (10**9 + 7)
