class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = max(piles)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.possible(piles, H, mid):
                right = mid
            else:
                left = mid
        if self.possible(piles, H, left):
            return left
        return right

    def possible(self, piles, H, K):
        time = 0
        for p in piles:
            time += math.ceil(p / K)
        return time <= H
