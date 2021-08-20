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
            stack = []
            for job in range(day, num_jobs):
                dp[day][job] = dp[day - 1][job - 1] + jobDifficulty[job]
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[job]:
                    index = stack.pop()
                    dp[day][job] = min(dp[day][job], dp[day][index] - jobDifficulty[index] + jobDifficulty[job])
                if stack:
                    dp[day][job] = min(dp[day][job], dp[day][stack[-1]])
                stack.append(job)
        return dp[-1][-1]
