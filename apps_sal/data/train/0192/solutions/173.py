from collections import deque

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ret = 0
        
        d = deque(sorted(piles))
        
        def draw(ds):
            nonlocal ret
            discard = ds.pop()
            ret += ds.pop()
            discard = ds.popleft()
            
            return ds
            
            
        
        while len(d) >= 3:
            d = draw(d)
            
        return ret

