class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def enough(n):
            hrs = 0
            for i in piles:
                if n > i:
                    hrs += 1
                elif i % n == 0:
                    hrs += i // n
                else:
                    hrs += (i // n) + 1
            return hrs <= H

        l, r = 1, sum(piles)
        while l < r:
            m = (l + r) // 2
            if not enough(m):
                l = m + 1
            else:
                r = m
        return l
