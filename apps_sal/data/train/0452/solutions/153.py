class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def helper(st, d):
            if st == len(jobDifficulty) or d == 0 or len(jobDifficulty) - st < d:
                return math.inf
            if d == 1:
                return max(jobDifficulty[st:])
            (mn, mx) = (float('inf'), float('-inf'))
            for i in range(st + 1, len(jobDifficulty) - d + 2):
                mx = max(mx, jobDifficulty[i - 1])
                s = mx + helper(i, d - 1)
                mn = min(s, mn)
            return mn
        res = helper(0, d)
        return res if res != float('inf') else -1
