class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            K = low + (high - low) // 2
            h = sum([(pile - 1) // K + 1 for pile in piles])
            if h <= H:
                high = K
            else:
                low = K + 1
        return low
