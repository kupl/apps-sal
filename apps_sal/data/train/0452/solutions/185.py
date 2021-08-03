class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        cache = {}

        def dfs(start, days):
            if (start, days) in cache:
                return cache[(start, days)]
            if N - start < days or start == N or days < 1:
                cache[(start, days)] = -1
            elif days == 1:
                cache[(start, days)] = max(jobDifficulty[start:])
            else:
                max_daily = float('-inf')
                min_all = float('inf')
                for end in range(start, N - days + 1):
                    max_daily = max(max_daily, jobDifficulty[end])
                    min_all = min(min_all, max_daily + dfs(end + 1, days - 1))
                cache[(start, days)] = -1 if min_all == float('inf') else min_all
            return cache[(start, days)]

        return dfs(0, d)
