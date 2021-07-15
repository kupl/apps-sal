class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        module = 10 ** 9 + 7
        
        
        
        self.m = {}
        
        def dfs(d,f,target):
            
            if d == 0 and target == 0:
                return 1
            
            if d == 0 and target != 0:
                return 0
            if d*f < target or d > target:
                return 0
            
            if (d, target) in self.m:
                return self.m[(d, target)]
            
            
            res  = 0
            for i in range(1, f+1):
                res = (res + dfs(d - 1, f, target - i)) % module

            self.m[(d,target)] = res
            return res

        return dfs(d,f,target)
            

