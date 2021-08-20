class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def isValid(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
            return total <= H
        (i, j) = (1, max(piles))
        while i < j:
            mid = i + (j - i) // 2
            if isValid(mid):
                j = mid
            else:
                i = mid + 1
        return i
