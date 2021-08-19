class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        print(dp)
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1
        "\n        numOfCoins = [float('inf') for x in range(amount + 1)]\n        numOfCoins[0] = 0\n        for coin in coins:\n            for num in range(len(numOfCoins)):\n                if coin <= num:\n                    numOfCoins[num] = min(numOfCoins[num], numOfCoins[num - coin] + 1)\n        return numOfCoins[amount] if numOfCoins[amount] != float('inf') else -1\n        "
