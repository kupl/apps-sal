class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        n = len(jobs)
        dp = [[math.inf] * n for _ in range(d)]
        
        max_job = 0
        for job in range(n):
            max_job = max(max_job, jobs[job])
            dp[0][job] = max_job
        
        for day in range(1, d):
            for last_job in range(day, n):
                dp[day][last_job] = min(
                    dp[day - 1][first_job - 1] + max(jobs[first_job:last_job + 1])
                    for first_job in range(day, last_job + 1)
                )
        
        return dp[-1][-1] if dp[-1][-1] != math.inf else -1
