class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def can_finish(k):
            h = 0
            for p in piles:
                (d, r) = divmod(p, k)
                if r:
                    d += 1
                h += d
            return h <= H
        l = 1
        r = max(piles)
        while l < r:
            m = (l + r) // 2
            if can_finish(m):
                r = m
            else:
                l = m + 1
        return l
