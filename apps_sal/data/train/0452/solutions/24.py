class Solution:

    def minDifficulty(self, A: List[int], d: int) -> int:
        seen = {}

        def func(sidx, d):
            if n - sidx < d:
                return float('inf')
            if d == 0:
                return float('inf') if sidx < n else 0
            if n - sidx == d:
                return sum(A[sidx:])
            if (sidx, d) not in seen:
                res = float('inf')
                cmax = A[sidx]
                for eidx in range(sidx, n):
                    if cmax < A[eidx]:
                        cmax = A[eidx]
                    res = min(res, cmax + func(eidx + 1, d - 1))
                seen[sidx, d] = res
            return seen[sidx, d]
        n = len(A)
        if n < d:
            return -1
        if n == d:
            return sum(A)
        return func(0, d)
