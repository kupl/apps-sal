class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = [[0 for _ in range(7)] for _ in range(n + 1)]
        dp[0][6] = 1
        for r in range(1, n + 1):
            for f in range(6):
                k = 1
                while(k <= rollMax[f] and r - k >= 0):
                    dp[r][f] += dp[r - k][6] - dp[r - k][f]
                    k += 1

            dp[r][6] = sum(dp[r][:6])
        return (dp[-1][-1]) % (10**9 + 7)
