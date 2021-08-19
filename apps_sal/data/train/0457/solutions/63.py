class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float('inf')] * (amount + 1)
        calculated = [False] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
                calculated[coin] = True
        for i in range(1, amount + 1):
            if not calculated[i]:
                candidates = [dp[i - coin] for coin in coins if i >= coin]
                if candidates:
                    dp[i] = min(candidates) + 1
                    calculated[i] = True
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]
