class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def eatingPossible(cap, piles, H):
            h = 0
            for pile in piles:
                h += pile // cap
                if pile % cap != 0:
                    h += 1
                if h > H:
                    return False
            return True
        piles.sort()
        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if eatingPossible(mid, piles, H):
                right = mid
            else:
                left = mid + 1
        return left
