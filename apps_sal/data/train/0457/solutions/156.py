class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        numOfCoins = [float('inf') for x in range(amount + 1)]
        numOfCoins[0] = 0
        for coin in coins:
            for num in range(len(numOfCoins)):
                if coin <= num:
                    numOfCoins[num] = min(numOfCoins[num], numOfCoins[num - coin] + 1)
        return numOfCoins[amount] if numOfCoins[amount] != float('inf') else -1
