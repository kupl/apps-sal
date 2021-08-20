class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def helper(speed):
            h = 0
            for p in piles:
                h += math.ceil(p / speed)
            return h
        if not piles or len(piles) == 0:
            return 0
        (start, end) = (1, max(piles))
        while start + 1 < end:
            mid = start + (end - start) // 2
            h = helper(mid)
            if h <= H:
                end = mid
            else:
                start = mid
        return start if helper(start) <= H else end
