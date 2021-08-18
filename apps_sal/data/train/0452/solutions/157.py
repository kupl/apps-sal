from functools import lru_cache


class Solution:
    @lru_cache(None)
    def recursive(self, i, k):
        if k == 1:
            return max(self.x[i:])
        m, ans = self.x[i], float('inf')
        for j in range(i + 1, self.n + 2 - k):
            ans = min(ans, m + self.recursive(j, k - 1))
            m = max(m, self.x[j])
        return ans

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        self.x, self.n = jobDifficulty, len(jobDifficulty)
        if self.n < d:
            return -1
        self.recursive.cache_clear()
        return self.recursive(0, d)
