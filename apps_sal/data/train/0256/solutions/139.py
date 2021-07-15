class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def simulate(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile / k)
            return hours
        lower = 1
        upper = 1
        for pile in piles:
            upper = max(upper, pile)
        while lower < upper:
            midpoint = (upper + lower) // 2
            if simulate(midpoint) > H:
                lower = midpoint + 1
            else:
                upper = midpoint
        return upper
