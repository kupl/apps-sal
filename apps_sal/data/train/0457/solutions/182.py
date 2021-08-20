class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize for i in range(amount + 1)]
        m = len(coins)
        dp[0] = 0
        for j in range(m):
            for i in range(amount + 1):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        if dp[-1] == sys.maxsize:
            return -1
        return dp[-1]
