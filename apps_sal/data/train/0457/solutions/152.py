class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        print(dp)
        
        for coin in coins:
            for i in range(len(dp)):
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
        
        '''
        numOfCoins = [float('inf') for x in range(amount + 1)]
        numOfCoins[0] = 0
        for coin in coins:
            for num in range(len(numOfCoins)):
                if coin <= num:
                    numOfCoins[num] = min(numOfCoins[num], numOfCoins[num - coin] + 1)
        return numOfCoins[amount] if numOfCoins[amount] != float('inf') else -1
        '''
