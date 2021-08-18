class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        l, r = 1, max(piles)

        while l < r:
            mid = l + (r - l) // 2

            if sum([-pile // mid for pile in piles]) < -H:

                l = mid + 1

            else:
                r = mid
        return l
