class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        memo = {}
        def helper(start, days):
            if (start, days) in memo:
                return memo[(start,days)]
            if start == N or days < 1 or N - start < days: 
                memo[(start, days)] = -1
            elif days == 1:
                memo[(start, days)] = max(jobDifficulty[start:])
            else:
                max_diff = float('-inf')
                min_total = float('inf')
                for i in range(start, N-days+1):
                    max_diff = max(max_diff, jobDifficulty[i])
                    min_total = min(min_total, max_diff + helper(i+1, days-1))
                memo[(start, days)] = -1 if min_total == float('inf') else min_total
            return memo[(start, days)]
        return helper(0, d)
