from functools import lru_cache
mod = 10**9+7

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:    

        @lru_cache(None)
        def calculation(pos: int, steps: int):
            if pos < 0 or pos >= arrLen:
                return 0
            if pos > steps:
                return 0            
            if pos == steps:
                return 1            
            
            return (calculation(pos+1, steps-1) + calculation(pos-1, steps-1) + calculation(pos, steps-1) ) % mod
        
        return calculation(0, steps)
        

