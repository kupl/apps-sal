from typing import List


class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        memo = {}

        def top_down(days_remaining, current_job_index):
            if days_remaining <= 0:
                return float('inf')
            if current_job_index >= len(jobDifficulty):
                return float('inf')
            if days_remaining == 1:
                return max(jobDifficulty[current_job_index:])
            if (days_remaining, current_job_index) in memo:
                return memo[days_remaining, current_job_index]
            min_cost = float('inf')
            for next_job_index in range(current_job_index + 1, len(jobDifficulty)):
                min_cost = min(min_cost, max(jobDifficulty[current_job_index:next_job_index]) + top_down(days_remaining - 1, next_job_index))
            memo[days_remaining, current_job_index] = min_cost
            return min_cost
        min_cost = top_down(d, 0)
        return min_cost if min_cost != float('inf') else -1
