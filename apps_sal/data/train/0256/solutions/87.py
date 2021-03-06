class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            m = l + (r - l) // 2
            h = 0
            for i in piles:
                h += math.ceil(i / m)
            if h > H:
                l = m + 1
            else:
                r = m
        return l
