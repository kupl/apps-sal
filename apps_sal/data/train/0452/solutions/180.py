import sys


class Solution:
    def minDifficulty(self, complexity: List[int], days: int) -> int:
        num_tasks = len(complexity)
        if num_tasks < days:
            return -1
        dp = [sys.maxsize] * (num_tasks + 1)
        dp[0] = 0

        for day in range(1, days + 1):
            for i in range(num_tasks, 0, -1):
                cur_max = 0
                dp[i] = sys.maxsize if i > day - 1 else dp[i]
                for k in range(i, day - 1, -1):
                    cur_max = max(cur_max, complexity[k - 1])
                    dp[i] = min(dp[i], dp[k - 1] + cur_max)
        print(dp)
        return dp[-1]
