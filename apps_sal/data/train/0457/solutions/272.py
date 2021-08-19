class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coinsNeeded = {}
        coinsNeeded[0] = 0
        for n in coins:
            coinsNeeded[n] = 1

        def findMinCoins(amount):
            # print(amount)
            if amount < 0:
                return float('inf')

            if amount in coinsNeeded:
                # coinsNeeded[amount] = min(coinsUsed, coinsNeeded[amount])
                return coinsNeeded[amount]

            for n in coins:
                # if amount-n>=0:
                coinsUsed = 1 + findMinCoins(amount - n)
                # if coinsUsed > 0:
                if amount in coinsNeeded:
                    coinsNeeded[amount] = min(coinsUsed, coinsNeeded[amount])
                else:
                    coinsNeeded[amount] = coinsUsed

            # if amount in coinsNeeded:
            return coinsNeeded[amount]
            # return -1

        findMinCoins(amount)
        # print(coinsNeeded)
        if coinsNeeded[amount] == float('inf'):
            return -1
        # if amount in coinsNeeded:
        return coinsNeeded[amount]
        # return -1
