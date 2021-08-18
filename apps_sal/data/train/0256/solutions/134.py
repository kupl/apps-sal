class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        n = len(piles)
        low, high = 1, max(piles)
        while (low + 1) < high:
            mid = low + ((high - low) // 2)
            used_hrs = self.calc_hours(piles, mid)
            if used_hrs > H:
                low = mid
            else:
                high = mid

        if self.calc_hours(piles, low) <= H:
            return low
        if self.calc_hours(piles, high) <= H:
            return high

    @staticmethod
    def calc_hours(piles, K):
        return sum(((pile - 1) // K + 1) for pile in piles)
