class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        maxB = max(piles)

        def getH(k):
            if not k:
                return float('inf')
            numHours = 0
            for pile in piles:
                numHours += pile // k + int(bool(pile % k))
            return numHours

        def bs(start, end):
            if start > end:
                return float('inf')
            mid = (start + end + 1) // 2
            h = getH(mid)
            if h < H:
                if mid != start:
                    return min(mid, bs(start, mid - 1))
            if h > H:
                return bs(mid + 1, end)
            if h == H:
                while getH(mid - 1) == H:
                    mid -= 1
            return mid

        return bs(0, maxB)
