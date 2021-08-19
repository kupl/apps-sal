import math


class Solution:

    def cc(self, l, n):
        ans = 0
        for i in l:
            ans += math.ceil(i / n)
        return ans

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        n = len(piles)
        if H == n:
            return max(piles)
        else:
            l = math.ceil(sum(piles) / H) - 1
            r = max(piles) + 1
            while r - l > 1:
                pivot = (l + r) // 2
                if self.cc(piles, pivot) <= H:
                    r = pivot
                elif self.cc(piles, pivot) > H:
                    l = pivot
            return r
