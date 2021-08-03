
class Solution:
    def minEatingSpeed(self, piles, H):
        start = sum(piles) // H + 1
        while start <= max(piles):
            suplus = sum(map(lambda x: (start - x % start) % start, piles))
            if suplus + sum(piles) <= start * H:
                return start
            else:
                start += 1
        return max(piles)
