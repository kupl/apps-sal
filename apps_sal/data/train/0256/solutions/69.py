class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        right = 10**9
        left = 1
        piles.sort()
        while left + 1 < right:
            mid = (left + right)//2
            if self.canEatAll(piles, mid, H):
                right = mid
            else:
                left = mid
        return left if self.canEatAll(piles, left, H) else right
        

    def canEatAll(self, piles, speed, H):
        res = 0
        for pile in piles:
            res += (pile - 1)//speed + 1
        return res <= H

