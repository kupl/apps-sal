class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if not piles:
            return 0
        (l, r) = (1, max(piles))

        def canDo(k):
            ans = 0
            for v in piles:
                ans -= -v // k
            return ans <= H
        while l < r:
            m = (l + r) // 2
            if canDo(m):
                r = m
            else:
                l = m + 1
        return l
