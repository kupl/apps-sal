class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(coins, rem, count): #count is a list
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if count[rem-1] != 0: return count[rem-1]
            minVal = float('inf')
            for c in coins:
                res = helper(coins, rem-c, count)
                if res >= 0 and res < minVal:
                    minVal = 1 + res;
            if minVal == float('inf'):
                count[rem-1] = -1
            else:
                count[rem-1] = minVal
            return count[rem-1]
        
        if amount < 1:
            return 0
        return helper(coins, amount, [0]*amount)
