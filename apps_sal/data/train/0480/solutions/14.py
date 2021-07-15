class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        self.memo = {}
        def dfs(steps, pos):
            if pos < 0 or pos >= arrLen or pos>steps:
                return 0
            
            if steps == 0:
                if pos == 0:
                    return 1
                return 0
            
            if self.memo.get((steps, pos), None) is not None:
                return self.memo.get((steps, pos))
            
            ret = dfs(steps-1, pos-1)
            ret = ret % (10**9+7)
            ret += dfs(steps-1, pos)
            ret = ret % (10**9+7)
            ret += dfs(steps-1, pos+1)
            ret = ret % (10**9+7)
            
            self.memo.update({(steps, pos): ret})
            
            return ret
        
        return dfs(steps, 0)
