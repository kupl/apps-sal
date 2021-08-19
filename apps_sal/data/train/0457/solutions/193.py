class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize - 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            # if dp[i] == sys.maxsize-1:
            # continue
            for c in coins:
                if c + i <= amount:
                    dp[c + i] = min(dp[c + i], dp[i] + 1)
        if dp[-1] == sys.maxsize - 1:
            return -1
        return dp[-1]
