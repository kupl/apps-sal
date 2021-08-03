from functools import lru_cache


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        n = len(jobDifficulty)
        if n < d:
            return -1

        @lru_cache(None)
        def helper(i, d):
            nonlocal jobDifficulty, n

            if i >= n and d != 0:
                return float('inf')
            if d == 1:
                return max(jobDifficulty[i:])

            max_till_now = float('-inf')
            ans = float('inf')

            for j in range(i, n - d + 1):
                max_till_now = max(max_till_now, jobDifficulty[j])
                ans = min(ans, max_till_now + helper(j + 1, d - 1))
            return ans

        return helper(0, d)
