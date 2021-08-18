class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        n = len(piles)
        piles.sort()

        def finish(k):
            return sum((p - 1) // k + 1 for p in piles) <= H

        r = 0
        while r < n:
            if finish(piles[r]):
                break
            else:
                r += 1

        start = 1 if r == 0 else piles[0]
        end = piles[r]

        while start < end:
            mid = (start + end) // 2
            if finish(mid):
                end = mid
            else:
                start = mid + 1
        return start
