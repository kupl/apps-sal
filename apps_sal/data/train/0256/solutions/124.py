class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        mini = 1
        maxi = max(piles)
        ans = 0
        while mini <= maxi:
            mid = mini + (maxi - mini) // 2
            value = sum(((p - 1) // mid + 1 for p in piles))
            if value <= H:
                ans = mid
                maxi = mid - 1
            else:
                mini = mid + 1
        return ans
