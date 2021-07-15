class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        self.ret = float('inf')


        
        def recurrent(index, coins, amount, current):    
            first = coins[index]
            n = amount // first
            remainder = amount % first
            if remainder == 0:
                self.ret = min(self.ret, current + n)
            else:
                l = len(coins)
                while remainder <= amount and index<l-1 and current + n < self.ret:
                    recurrent(index+1, coins, remainder, current + n)
                    n -= 1
                    remainder += first

            return
        
        
        
        recurrent(0, coins, amount, 0)
        
        
        
        if self.ret == float('inf'):
            return -1
        else:
            return self.ret
        


