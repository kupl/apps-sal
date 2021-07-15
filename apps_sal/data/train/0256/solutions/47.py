class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if H == len(piles):
            return max(piles)
        
        l = 1
        r = max(piles) + 1
        while l < r:
            m = l + (r - l) // 2
            if self.minHours(piles, m) <= H:
                r = m
            elif self.minHours(piles, m) > H:
                l = m + 1
        return l
        
        
    def minHours(self, piles, k):
        h = 0
        for p in piles:
            if p % k == 0:
                h += p // k
            else:
                h = h + p // k + 1
        return h
        

