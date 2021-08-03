class Solution:
    def canEat(self, piles, bananas, H):
        cur_H = 0
        for pile in piles:
            if pile % bananas == 0:
                cur_H += pile // bananas
            else:
                cur_H += pile // bananas + 1
        if cur_H > H:
            return False
        return True

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        min_speed = 1
        max_speed = max(piles)
        while(min_speed < max_speed):
            mid = (min_speed + max_speed) // 2
            if self.canEat(piles, mid, H):
                max_speed = mid
            else:
                min_speed = mid + 1
        return min_speed
