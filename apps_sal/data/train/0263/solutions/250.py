class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        ret = 0
        dp = [[0] * 10 for i in range(n)]
        for i in range(10):
            dp[0][i] = 1
        graph = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        for i in range(1, n):
            for j in range(10):
                for neighbor in graph[j]:
                    dp[i][j] += dp[i - 1][neighbor]
        ret = sum((dp[n - 1][i] for i in range(10)))
        return ret % (10 ** 9 + 7)
