class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        seen = {}

        def minDifficultyRestOfJobs(start, days_left):

            if (start, days_left) in seen:
                return seen[(start, days_left)]

            if len(jobDifficulty[start:]) < days_left:
                return float('inf')

            if days_left == 1:
                return max(jobDifficulty[start:])

            max_difficulty_today, total_difficulty = float('-inf'), float('inf')
            for job_idx in range(start, len(jobDifficulty)):
                max_difficulty_today = max(max_difficulty_today, jobDifficulty[job_idx])
                total_difficulty = min(total_difficulty, max_difficulty_today + minDifficultyRestOfJobs(job_idx + 1, days_left - 1))

            seen[(start, days_left)] = total_difficulty

            return total_difficulty

        res = minDifficultyRestOfJobs(0, d)
        return -1 if res == float('inf') else res
