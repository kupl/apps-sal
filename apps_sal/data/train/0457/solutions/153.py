class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # brute force keep looking for ways until it == 0
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # store the number of ways to 0

        for coin in coins:  # check if dp[i] > coin then return the min
            for i in range(1, amount + 1):
                if i - coin >= 0:  # valid combination
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] < float('inf'):
            return dp[-1]
        return -1
