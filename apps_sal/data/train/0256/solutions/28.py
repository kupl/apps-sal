class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            if self.get_total_days(piles, mid) > H:
                left = mid + 1
            else:
                right = mid
        return left

    def get_total_days(self, piles: List[int], num_eat: int) -> int:
        if num_eat == 0:
            return 0
        total_days = 0
        for pile in piles:
            total_days += math.ceil(float(pile) / num_eat)
        return total_days
