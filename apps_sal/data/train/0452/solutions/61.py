class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        @lru_cache(None)
        def find_schedule(remaining_days, task_start):
            if remaining_days == 0:
                return max(jobDifficulty[task_start:])
            total = float('inf')
            cur_diff = jobDifficulty[task_start]
            for i in range(task_start, len(jobDifficulty) - remaining_days):
                cur_diff = max(cur_diff, jobDifficulty[i])
                total = min(total, cur_diff + find_schedule(remaining_days - 1, i + 1))
            return total
        if len(jobDifficulty) < d:
            return -1
        return find_schedule(d - 1, 0)
