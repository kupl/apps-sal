import math as m


class Solution:
    def check_time(piles, speed):
        hrs = 0
        for i in piles:
            hrs += int(m.ceil(i / speed))
        return hrs

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        low = 1
        high = float('-inf')
        for i in piles:
            high = max(high, i)
        if H == len(piles):
            return high
        while(low <= high):
            mid = (low + high) // 2
            hrs = Solution.check_time(piles, mid)
            if hrs > H:
                low = mid + 1
            else:
                high = mid - 1
        return low
