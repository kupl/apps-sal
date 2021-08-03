class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]
        length = len(coins)
        for i in range(1, amount + 1):
            dp += [9999]
            for j in range(length):
                if i >= coins[j] and dp[int(i - coins[j])] != 9999:
                    dp[i] = min(dp[i], dp[int(i - coins[j])] + 1)
        if dp[amount] == 9999:
            return -1
        return dp[amount]
