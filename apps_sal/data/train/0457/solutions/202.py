class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None for i in range(0, amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            min_cost = float('inf')
            for j in range(0, len(coins)):
                if coins[j] <= i:
                    min_cost = min(min_cost, dp[i - coins[j]] + 1)
            dp[i] = min_cost
        if dp[-1] > amount:
            return -1
        return dp[-1]
        coinsNeeded = {}
        coinsNeeded[0] = 0
        for n in coins:
            coinsNeeded[n] = 1

        def findMinCoins(amount):
            if amount < 0:
                return float('inf')
            if amount in coinsNeeded:
                return coinsNeeded[amount]
            for n in coins:
                coinsUsed = 1 + findMinCoins(amount - n)
                if amount in coinsNeeded:
                    coinsNeeded[amount] = min(coinsUsed, coinsNeeded[amount])
                else:
                    coinsNeeded[amount] = coinsUsed
            return coinsNeeded[amount]
        findMinCoins(amount)
        if coinsNeeded[amount] == float('inf'):
            return -1
        return coinsNeeded[amount]
