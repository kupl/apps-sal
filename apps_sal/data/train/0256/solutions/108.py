class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if len(piles) == 1:
            return piles[0] // H if piles[0] % H == 0 else piles[0] // H + 1
        l = sum(piles) // H
        h = max(piles) * len(piles) // H + 1

        def feasible(k):
            return sum(((p - 1) // k + 1 for p in piles)) <= H
        while l < h:
            mid = (l + h) // 2
            if feasible(mid):
                h = mid
            else:
                l = mid + 1
        return l
