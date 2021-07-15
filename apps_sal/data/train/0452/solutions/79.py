class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        @lru_cache(None)
        def go(l, day):
            if l >= n:
                return math.inf
            if day == d:
                return max(jobDifficulty[l:])
            ans = math.inf
            for i in range(l, n):
                ans = min(ans, go(i+1, day+1) + max(jobDifficulty[l:i+1]))
            return ans
        return go(0, 1)

