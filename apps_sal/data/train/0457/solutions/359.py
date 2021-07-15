class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
            
        def helper(coins, rem, counts):
            if rem < 0: return -1
            if rem == 0: return 0
            if counts[rem-1] != 0: return counts[rem-1]
            min_val = float('inf')
            for coin in coins:
                res = helper(coins, rem - coin, counts)
                if res >= 0 and res < min_val:
                    min_val = res + 1
                if min_val == float('inf'):
                    counts[rem - 1] = -1
                else:
                    counts[rem - 1] = min_val
            return counts[rem-1]
        
        if amount < 1: return 0
        return helper(coins, amount, [0]*amount)
