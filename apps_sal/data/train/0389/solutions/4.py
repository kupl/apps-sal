

from functools import lru_cache


class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        n, total = len(A), sum(A)

        @lru_cache(None)
        def dfs(idx, target, sz):

            if target < 0 or idx + sz > n:
                return False
            if sz == 0:
                return target == 0

            return dfs(idx + 1, target - A[idx], sz - 1) or dfs(idx + 1, target, sz)
        return any(dfs(0, total * k // n, k) for k in range(1, n // 2 + 1) if total * k % n == 0)
