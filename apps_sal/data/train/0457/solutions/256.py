class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = {}
        for c in coins:
            dp[c] = 1
        for i in range(amount + 1):
            for c in coins:
                if dp.get(i - c):
                    if not dp.get(i):
                        dp[i] = dp[i - c] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - c] + 1)
        return dp.get(amount, -1)
