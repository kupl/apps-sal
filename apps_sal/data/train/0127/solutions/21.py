from functools import lru_cache


class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:

        C = len(group)
        MOD = pow(10, 9) + 7

        dp = [[0] * (P + 1) for _ in range(G + 1)]
        dp[0][0] = 1
        for c in range(1, C + 1):
            g = group[c - 1]
            p = profit[c - 1]
            for i in range(G, g - 1, -1):
                for j in range(P, -1, -1):
                    dp[i][j] = (dp[i][j] + dp[i - g][max(0, j - p)]) % MOD

        return sum(dp[i][P] for i in range(G + 1)) % MOD
