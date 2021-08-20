class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        coins.sort()
        for i in range(amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coins[j]])
                else:
                    break
        if dp[-1] == amount + 1:
            return -1
        else:
            return dp[-1]
