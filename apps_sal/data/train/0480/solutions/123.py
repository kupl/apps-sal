from functools import lru_cache
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @lru_cache(maxsize=None)
        def cc(step, pos):
            if step == steps:
                return 1 if pos == 1 else 0
            else:
                if pos == 1:
                    return cc(step+1, pos+1) + cc(step+1, pos)
                elif pos == arrLen:
                    return cc(step+1, pos-1) + cc(step+1, pos)
                else:
                    return cc(step+1, pos+1) + cc(step+1, pos-1) + cc(step+1, pos)
        mod = int(10 **9 + 7)
        return cc(0, 1) % mod
                    
        

