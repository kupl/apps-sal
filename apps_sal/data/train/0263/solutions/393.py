import numpy as np


class Solution:
    def knightDialer(self, N: int) -> int:
        goto = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        dp = np.zeros((10, N)).astype(int)

        dp[:, 0] = 1

        for c in range(1, N):
            for p in range(10):
                for next_vals in goto[p]:
                    dp[p, c] += dp[next_vals, c - 1] % (10**9 + 7)

        return int(sum(dp[:, N - 1])) % (10**9 + 7)
