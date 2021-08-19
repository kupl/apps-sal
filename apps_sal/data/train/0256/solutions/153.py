class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # wants to eat all bananas within H hours
        # K - speed at which eat banana
        # can eat up to pile[i] banana
        # cannot eat 2 piles in 1 hour
        # return min K to eat all bananas in H hours

        def get_hours_needed(piles, K):
            hours_needed = 0
            for pile in piles:
                hours_needed += pile // K
                if pile % K != 0:
                    hours_needed += 1
            return hours_needed

        lo = 1
        hi = max(piles)

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if get_hours_needed(piles, mid) > H:
                lo = mid + 1
            else:  # hours_needed <= H
                hi = mid

        return lo
