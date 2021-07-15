class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        memo = {}
        def dfs(step, rest_amount):
            if rest_amount < 0:
                return -1
            if rest_amount == 0:
                return 0 
            
            if rest_amount in memo:
                return memo[rest_amount]
            min_steps = math.inf
            for coin in coins:
                rest = rest_amount - coin
                #print(c, rest, step)
                res =  dfs(step+1, rest)
                if res >= 0:
                    min_steps = min(min_steps, res)
            
            
            memo[rest_amount] = min_steps + 1 if min_steps != math.inf else -1
            return memo[rest_amount]
                
                
        
        res = dfs(0, amount)
        return res
            

