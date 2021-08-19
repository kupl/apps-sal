class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        if n // 2 == 0:
            return True
        dp = [[0 for i in range(n)] for j in range(n)]
        prefix = [0]
        for i in range(n):
            dp[i][i] = piles[i]
            prefix.append(prefix[-1] + piles[i])
        for k in range(1, n):
            for i in range(n):
                j = i + k
                if j >= n:
                    break
                dp[i][j] = piles[j] + (prefix[j] - prefix[i] - dp[i][j - 1])
                dp[i][j] = max(dp[i][j], piles[i] + (prefix[j + 1] - prefix[i + 1] - dp[i + 1][j]))
        return dp[0][-1] > sum(piles) // 2
