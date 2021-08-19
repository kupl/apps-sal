class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def can(K):
            cur = H
            for a in piles:
                cur -= a // K
                cur -= a % K != 0
            return cur >= 0
        (l, r) = (1, sum([a + 1 for a in piles]))
        while l < r:
            mid = (l + r) // 2
            if can(mid):
                r = mid
            else:
                l = mid + 1
        return l
