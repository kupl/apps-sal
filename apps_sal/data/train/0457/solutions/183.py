class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount:
            dp = [float('inf')] * amount
            for j in range(amount):
                if j + 1 in coins:
                    dp[j] = 1
                else:
                    for c in coins:
                        if j - c + 1 > 0:
                            dp[j] = min(dp[j], dp[j - c] + 1)
            if dp[amount - 1] < float('inf'):
                return dp[amount - 1]
            else:
                return -1
        else:
            return 0
