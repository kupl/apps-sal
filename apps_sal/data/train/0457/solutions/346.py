class Solution:
    # Top down DP solution
    def helper(self, coins, amount, dp):
        if amount < 0:
            # cant get a negative amount - need inf coins
            return float('inf')
        if amount == 0:
            # if amount is 0, we need to use 0 coins
            return 0
        if amount in dp:
            # already cached
            return dp[amount]
        for i in range(len(coins)):
            # We use coin i so now amount is amount - coins[i]
            use_ci = 1 + self.helper(coins, amount - coins[i], dp)
            if amount not in dp:
                dp[amount] = use_ci
            else:
                # either using this coin makes it fewer coins or not
                dp[amount] = min(dp[amount], use_ci)
        return dp[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0
        dp = {}  # dp cache | memoization
        result = self.helper(coins, amount, dp)
        return -1 if result == float('inf') else result
