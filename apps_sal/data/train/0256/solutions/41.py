import math

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        n = len(piles)
        s = sum(piles)
        
        if H == n:
            return max(piles)
        
        if H > s:
            return 1
        
        k = s // H
        i = 0
        while True:
            t = 0
            for j in range(len(piles)):
                t += math.ceil(piles[j] / k)
            if t <= H:
                return k
            k += 1
        
        return 0
