from collections import defaultdict

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        self.counter = 0
        cache = defaultdict(defaultdict)
       
        def rec(pos, steps):
            if pos in cache:
                if steps in cache[pos]:
                    return cache[pos][steps]
                
            if steps == 0:
                if pos == 0:
                    return 1
                return
            if pos < 0 or pos >= arrLen:
                return
           
            if steps < pos:
                return
            
            left = rec(pos-1, steps-1)
            right = rec(pos+1, steps-1)
            stay = rec(pos, steps-1)
            if left is None and right is None and stay is None:
                val = None
            else:
                val = (left or 0) + (right or 0) + (stay or 0)
                
            cache[pos][steps] = val
            return val
        
        res = rec(0, steps) 
        
        return res % (10**9 + 7)

