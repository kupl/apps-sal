class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = [0] * n
        # i is rightbound
        for i in range(n):
            # j is leftbound
            for j in range(i, -1, -1):
                if i == j:
                    dp[i] = piles[i]
                else:
                    dp[j] = max(piles[i] - dp[j], piles[j] - dp[j+1])
        return dp[0] > 0
