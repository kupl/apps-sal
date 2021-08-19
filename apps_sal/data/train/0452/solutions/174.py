from functools import lru_cache


class Solution:

    def minDifficulty(self, A: List[int], d: int) -> int:
        if len(A) < d:
            return -1

        @lru_cache(None)
        def helper(i, d):
            if i == len(A):
                if d == 0:
                    return 0
                return float('inf')
            if d == 0:
                return float('inf')
            res = float('inf')
            local_max = float('-inf')
            for j in range(i, len(A)):
                local_max = max(local_max, A[j])
                res = min(res, local_max + helper(j + 1, d - 1))
            return res
        res = helper(0, d)
        return res if res < float('inf') else -1
