class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        cache = [0] * (amount+1)
        for i in range(1, amount+1):
            min_count = float('inf')
            
            for coin in coins:
                if i-coin >= 0:
                    current_min_coin = cache[i-coin] + 1
                    if min_count > current_min_coin:
                        min_count = current_min_coin
                        
            cache[i] = min_count
        
        if cache[amount] in [0, float('inf')]:
            return -1
            
        return cache[amount]

