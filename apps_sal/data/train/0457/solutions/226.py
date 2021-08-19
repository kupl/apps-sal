class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        numCoins = [float('inf') for i in range(amount)]
        for coin in coins:
            if coin - 1 < amount:
                numCoins[coin - 1] = 1
        for i in range(amount):
            minCoin = float('inf')
            change = True
            for coin in coins:
                if i == coin - 1:
                    change = False
                    break
                if i - coin >= 0:
                    minCoin = min(numCoins[i - coin], minCoin)
            if change and minCoin != float('inf'):
                numCoins[i] = minCoin + 1
            # print(numCoins)
        if numCoins[-1] == float('inf'):
            return -1
        return numCoins[-1]
