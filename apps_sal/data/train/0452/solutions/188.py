class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        num_jobs = len(jobDifficulty)
        if num_jobs < d:
            return -1

        dp = [[-1 for _ in range(num_jobs)] for _ in range(d)]

        max_so_far = -math.inf
        for job in range(num_jobs):
            max_so_far = max(max_so_far, jobDifficulty[job])
            dp[0][job] = max_so_far

        for day in range(1, d):
            for job in range(day, num_jobs):
                max_so_far = -math.inf
                for backwards_walker in range(job, day - 1, -1):
                    max_so_far = max(max_so_far, jobDifficulty[backwards_walker])
                    dp[day][job] = min(dp[day][job], max_so_far + dp[day - 1][backwards_walker - 1]) if dp[day][job] != -1 else max_so_far + dp[day - 1][job - 1]
        print(dp)
        return dp[-1][-1]
