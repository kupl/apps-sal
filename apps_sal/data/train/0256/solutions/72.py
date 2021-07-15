class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if len(piles) == 1:
            div, rem = divmod(piles[0], H)
            if rem == 0:
                return div
            else:
                return div + 1
        left = 0
        right = sum(piles)
        while left < right:
            mid = (left + right) // 2
            if self.CalcTime(piles, mid, H):
                right = mid
            else:
                left = mid + 1
        return left
        
    def CalcTime(self, piles, K, H):
        h = 0
        for p in piles:
            div, rem = divmod(p, K)
            h += div
            if rem > 0:
                h += 1
            if h > H:
                return False
        return h <= H

