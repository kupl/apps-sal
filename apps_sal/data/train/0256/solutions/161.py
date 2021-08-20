class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        K = sum(piles) // H
        if K == 0:
            K = 1
        while True:
            hours_needed = 0
            for pile in piles:
                hours_needed += pile // K
                if pile % K != 0:
                    hours_needed += 1
            if hours_needed <= H:
                return K
            K += 1
