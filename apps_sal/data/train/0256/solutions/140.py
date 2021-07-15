class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        def possible(K):
            return sum(math.ceil(p/ K) for p in piles) <= H

        N = len(piles)
        if H == N:
            return max(piles)
        sm = sum(piles)
        lo, hi = int(sm/H)+1, math.ceil(sm/(H-N))
        while lo < hi:
            mi = (lo + hi) // 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return hi

