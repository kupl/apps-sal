class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @lru_cache(None)
        def helper(start, d):
            if len(jobDifficulty) - start < d:
                return float('inf')
            if d == 1:
                return max(jobDifficulty[start:])
            result = float('inf')
            for i in range(start, len(jobDifficulty) - d + 1):
                result = min(result, max(jobDifficulty[start:i+1]) + helper(i+1, d-1))
            return result
        result = helper(0, d)
        return result if result != float('inf') else -1
