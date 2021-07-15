class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        self.min = 2**31-1

        def dfs(index, amount, count):
            if amount==0:
                self.min = min(self.min, count)
            if amount < 0:
                return 
            for i in range(index, len(coins)):
                if coins[i] * (self.min-count)>amount >= coins[i]: # if hope still exists
                    dfs(i, amount-coins[i], count+1)
                    
        dfs(0, amount, 0)
        return self.min if self.min != 2**31-1 else -1
