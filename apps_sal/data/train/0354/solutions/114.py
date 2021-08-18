class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        dp = [[0] * 7 for _ in range(n)]
        dp[0] = [1] * 6 + [6]

        for r in range(1, n):
            for c in range(6):

                dp[r][c] = dp[r - 1][-1]

                k = r - rollMax[c]

                if k == 0:
                    dp[r][c] -= 1

                elif k >= 1:
                    dp[r][c] -= (dp[k - 1][-1] - dp[k - 1][c])

            dp[r][6] = sum(dp[r][:6])

        return dp[-1][-1] % int(1e9 + 7)
