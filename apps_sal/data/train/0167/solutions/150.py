class Solution:

    @lru_cache(None)
    def superEggDrop(self, k: int, n: int) -> int:
        if n == 0:
            return 0
        elif k == 1:
            return n
        (lo, hi) = (1, n)
        while lo < hi:
            mid = (lo + hi) // 2
            (r1, r2) = (self.superEggDrop(k - 1, mid - 1), self.superEggDrop(k, n - mid))
            if r1 > r2:
                hi = mid
            elif r1 < r2:
                lo = mid + 1
            else:
                lo = hi = mid
        return 1 + max(self.superEggDrop(k - 1, lo - 1), self.superEggDrop(k, n - lo))
