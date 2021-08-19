class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        lower_bound = 1
        upper_bound = sum(piles)
        while lower_bound < upper_bound:
            speed = (lower_bound + upper_bound) // 2
            if self.can_finish(piles, speed, H):
                upper_bound = speed
            else:
                lower_bound = speed + 1
        return upper_bound

    def can_finish(self, piles, speed, h):
        hours = 0
        for bananas in piles:
            hours += math.ceil(bananas / speed)
        return hours <= h
