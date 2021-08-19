class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def ifeatK(k):
            hour = 0
            for pile in piles:
                hour += math.ceil(pile / k)
            return hour
        start = 1
        end = sum(piles)
        while start + 1 < end:
            mid = (start + end) // 2
            if ifeatK(mid) < H:
                end = mid
            elif ifeatK(mid) > H:
                start = mid
            else:
                end = mid
        if ifeatK(start) > H:
            return end
        if ifeatK(start) == H:
            return start
        if ifeatK(end) == H:
            return end
        return start
