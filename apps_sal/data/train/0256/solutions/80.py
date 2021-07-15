class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            m = l + (r-l)//2
            if self.speedBalancer(piles, m) > H:
                l = m + 1
            elif self.speedBalancer(piles, m) <= H:
                r = m - 1
        return l
                
                
    def speedBalancer(self, piles, target):
        h = 0
        for i in piles:
            h += i // target
            if i % target != 0:
                h += 1
        return h
