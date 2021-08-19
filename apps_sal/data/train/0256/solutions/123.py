class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            hours = sum(((x - 1) // mid + 1 for x in piles))
            if hours <= H:
                right = mid - 1
            else:
                left = mid + 1
        return left
