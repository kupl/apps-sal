class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9+7
        memory = {}
        
        def helper(i, steps):
            if i < 0 or i == arrLen:
                return 0
            if i > steps:
                return 0
            if i == steps:
                return 1
            prev = memory.get((i, steps))
            if prev is not None:
                return prev

            stay = helper(i, steps-1)
            left = helper(i-1, steps-1)
            right = helper(i+1, steps-1)
            
            result = (stay + left + right) % MOD
            memory[(i, steps)] = result
            
            return result
        
        return helper(0, steps) 
