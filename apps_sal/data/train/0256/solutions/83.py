class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        n = len(piles)
        if n >= H:
            return max(piles)
        def check(m):
            ret = 0
            for p in piles:
                ret += p//m + (p%m!=0)
            return ret
        upper = max(piles)
        lo, hi = 1, upper
        while lo<=hi:
            mid = (lo+hi)//2
            if check(mid) <= H:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

