class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        piles.sort()
        (l, r) = (1, max(piles))
        while l <= r:
            m = (l + r) // 2
            if sum([(x - 1) // m + 1 for x in piles]) > H:
                l = m + 1
            elif sum([math.ceil(x / m) for x in piles]) < H:
                r = m - 1
            else:
                return m
        return l
