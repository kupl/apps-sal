class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            p = l + (r - l) // 2
            if sum(math.ceil(x / p) for x in piles) > H:
                l = p + 1
            else:
                r = p
        return l
