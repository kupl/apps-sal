class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        num_jobs = len(jobDifficulty)
        if num_jobs < d:
            return -1

        # The dp cache only keeps the best value up to that point for that number of days
        # This can be further optimized to only need two arrays since we only look at the previous row
        dp = [[-1 for _ in range(num_jobs)] for _ in range(d)]

        # First day everything is just the max up to that point
        max_so_far = -math.inf
        for job in range(num_jobs):
            max_so_far = max(max_so_far, jobDifficulty[job])
            dp[0][job] = max_so_far

        # Now do the rest
        for day in range(1, d):
            # In order to determine best difficulty, keep monotonic decreasing stack of difficulties
            # This will retain useful information up to each value and remove the need to loop backwards
            stack = []
            for job in range(day, num_jobs):  # Must be at least as many days as jobs
                # This value on its own plus the best of the previous
                dp[day][job] = dp[day - 1][job - 1] + jobDifficulty[job]
                # Keep stack in decreasing order
                while stack and jobDifficulty[stack[-1]] <= jobDifficulty[job]:
                    index = stack.pop()
                    dp[day][job] = min(dp[day][job], dp[day][index] - jobDifficulty[index] + jobDifficulty[job])
                if stack:
                    dp[day][job] = min(dp[day][job], dp[day][stack[-1]])

                stack.append(job)

        return dp[-1][-1]
