class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        use dp 0 - 11
        """
        if amount == 0:
            return 0
        dp = [float('inf')] * amount
        for i in range(0, amount):
            for c in coins:
                if (i + 1) % c == 0:
                    dp[i] = min(dp[i], (i + 1) // c)
                elif i + 1 > c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[-1] == float('inf') else dp[-1]
