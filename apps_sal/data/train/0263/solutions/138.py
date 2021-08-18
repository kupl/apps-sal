class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        mappings = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6],
        }

        dp = [[0 for i in range(10)] for i in range(n + 1)]
        dp[0] = [1 for i in range(10)]
        dp[1] = [len(mappings[i]) for i in range(10)]

        for i in range(1, n - 1):
            for j in range(10):
                pos = mappings[j]
                for k in pos:
                    dp[i + 1][k] += dp[i][j]

        return sum(dp[n - 1]) % MOD
