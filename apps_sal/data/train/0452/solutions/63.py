class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)

        @lru_cache(None)
        def dfs(index, days_left, curr_max):
            if index == N:
                if days_left == 0:
                    return curr_max
                else:
                    return float('inf')
            res = float('inf')
            same_day = dfs(index + 1, days_left, max(curr_max, jobDifficulty[index]))
            diff_day = dfs(index + 1, days_left - 1, jobDifficulty[index]) + curr_max
            res = min(same_day, diff_day)
            return res
        res = dfs(0, d, 0)
        if res == float('inf'):
            return -1
        else:
            return res
