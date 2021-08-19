from math import ceil


class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        hi_fail = 0
        low_pass = max(piles)
        if len(piles) == H:
            return low_pass
        piles.sort(reverse=True)
        speed = low_pass // 2
        while low_pass - hi_fail > 1:
            for (i, num_bananas) in enumerate(piles):
                if num_bananas <= speed:
                    break
            else:
                i += 1
            if not self.can_eat_all(piles, H, speed, i):
                hi_fail = speed
            else:
                low_pass = speed
            speed = (low_pass + hi_fail) // 2
        return low_pass

    def can_eat_all(self, piles, hours, speed, stop_ind):
        extra_hours = hours - len(piles)
        for i in range(stop_ind):
            hours_needed = int(ceil(piles[i] / speed))
            extra_hours -= hours_needed - 1
            if extra_hours < 0:
                return False
        if len(piles) == 1 and extra_hours == 0:
            return False
        return True
