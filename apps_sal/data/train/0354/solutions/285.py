class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * 7 for _ in range(n + 1)]
        dp[0][6] = 1
        for i in range(6):
            dp[1][i] = 1
        dp[1][6] = 6
        for i in range(2, n + 1):
            total_in_this_pos = 0
            for j in range(6):
                total = 0
                for k in range(max(0, i - rollMax[j]), i):
                    total += dp[k][6] - dp[k][j]
                dp[i][j] = total
                total_in_this_pos += total
            dp[i][6] = total_in_this_pos
        return dp[-1][-1] % MOD
