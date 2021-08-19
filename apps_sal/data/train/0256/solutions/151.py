class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        (left, right) = (1, max(piles))
        while left <= right:
            k = left + (right - left) // 2
            if self.finish(k, piles) <= H:
                right = k - 1
            else:
                left = k + 1
        return left

    def finish(self, k, piles):
        res = 0
        for pile in piles:
            res += pile // k
            if pile % k != 0:
                res += 1
        return res
