from functools import lru_cache

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        return self.toZero(n)
    
    @lru_cache(maxsize=None)
    def toZero(self, n):
        if n <= 1:
            return n
        elif n == 2:
            return 3
        elif n == 3:
            return 2
        
        offset = 0
        while ((1 << (offset + 1)) - 1) & n != n:
            offset += 1
        
        target = 1 << (offset - 1)
        return self.topower2(n & ((target << 1) - 1), target) + 1 + self.toZero(target)
    
    @lru_cache(maxsize=None)
    def topower2(self, n, target):
        if n == 0:
            return 1 + self.topower2(1, target)
        elif n == target:
            return 0
        
        offset = 0
        while ((1 << (offset + 1)) - 1) & n != n:
            offset += 1
             
        if n & target == 0:
            return self.topower2(n, target >> 1) + 1 + self.toZero(target >> 1)
        
        return self.toZero(n & (target - 1))
        

