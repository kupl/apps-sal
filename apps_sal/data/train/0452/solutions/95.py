class Solution:

    def minDifficulty(self, jobs: List[int], d: int) -> int:
        n = len(jobs)
        dp = [[math.inf] * n for _ in range(d)]
        max_job = 0
        for job in range(n):
            max_job = max(max_job, jobs[job])
            dp[0][job] = max_job
        for day in range(1, d):
            for job in range(day, n):
                cur = math.inf
                for prev in range(day, job + 1):
                    max_job = max(jobs[prev:job + 1])
                    cur = min(cur, dp[day - 1][prev - 1] + max_job)
                dp[day][job] = cur
        return dp[-1][-1] if dp[-1][-1] != math.inf else -1
