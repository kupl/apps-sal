class Solution:

    def knightDialer(self, n: int) -> int:
        dp = [[0] * 10 for _ in range(n)]
        pad_map = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        mod = 10 ** 9 + 7
        for i in range(10):
            dp[0][i] = 1
        for i in range(n - 1):
            for j in range(10):
                dsts = pad_map[j]
                for dst in dsts:
                    dp[i + 1][dst] = (dp[i][j] + dp[i + 1][dst]) % mod
        return sum(dp[-1]) % mod
