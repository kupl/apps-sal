class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()

        def recurse(amount, index):
            if (amount == 0):
                return 0

            if (amount in memo):
                return memo[amount]

            minCoins = float('inf')
            
            for coin in coins:
                if (amount - coin >= 0):
                    response = recurse(amount-coin, 0)
                    
                    if (response != -1):
                        minCoins = min(minCoins, response+1)
            
            memo[amount] = minCoins if minCoins != float('inf') else -1
            return memo[amount]
        
        return recurse(amount, 0)
