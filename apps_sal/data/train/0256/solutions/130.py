class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        K = sum(piles) // H + (sum(piles) % H != 0)
        while True:
            hours_needed = 0
            for pile in piles:
                hours_needed += pile // K + (pile % K != 0)
            if hours_needed <= H:
                return K
            K += 1
