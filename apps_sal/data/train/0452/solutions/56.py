class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        cache = {}
        self.helper(jobDifficulty, 0, d, cache)
        result = cache.get((0, d))
        return -1 if result is None or result == float('inf') else result

    def helper(self, jobDifficulty, i, d, cache):
        if (i, d) in cache:
            return cache[i, d]
        if i == len(jobDifficulty) and d == 0:
            return 0
        if d <= 0 or len(jobDifficulty) - i < d:
            return float('inf')
        maxVal = -1
        cache[i, d] = float('inf')
        for j in range(i, len(jobDifficulty)):
            maxVal = max(maxVal, jobDifficulty[j])
            result = maxVal + self.helper(jobDifficulty, j + 1, d - 1, cache)
            cache[i, d] = min(cache[i, d], result)
        return cache[i, d]
