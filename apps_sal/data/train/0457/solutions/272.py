class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
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
