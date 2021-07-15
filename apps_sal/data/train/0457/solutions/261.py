class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        d = {0:0}
        
        def dfs(left, num):
            if left < 0:
                return -1
            
            if left in d:
                return d[left]
            
            min_ans = math.inf
            for each in coins:
                val = dfs(left-each, num+1)
                if val >= 0:
                    min_ans = min(min_ans, val)
            
            if min_ans == math.inf:
                d[left] = -1
            else:
                d[left] = min_ans + 1
            
            return d[left]
        

        return dfs(amount, 0)
