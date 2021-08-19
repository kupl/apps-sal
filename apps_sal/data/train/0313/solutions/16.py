class Solution:

    def minDays(self, blooms: List[int], m: int, k: int) -> int:

        def check(d):
            (bouq, b) = (0, 0)
            for i in range(len(blooms)):
                if blooms[i] <= d:
                    b += 1
                else:
                    b = 0
                if b == k:
                    b = 0
                    bouq += 1
                    if bouq >= m:
                        return True
            return bouq >= m
        (lo, hi) = (1, max(blooms))
        while lo < hi:
            mid = (hi + lo) // 2
            if not check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo if check(lo) else -1
