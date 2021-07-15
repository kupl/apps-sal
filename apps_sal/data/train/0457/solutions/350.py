class Solution:
    
    def __init__(self):
        self.memo = {}
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = self.helper(coins,amount)
        if ans == float('inf'):
            return -1
        return ans
        
    def helper(self, coins, remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')
        if remaining in self.memo:
            return self.memo[remaining]
        self.memo[remaining] = min([self.helper(coins,remaining-i) for i in coins[::-1]])+1
        return self.memo[remaining]
        
        
        

