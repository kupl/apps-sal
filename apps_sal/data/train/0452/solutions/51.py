class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        memo = {}

        def dfs(idx, d):
            if (idx, d) in memo:
                return memo[idx, d]
            if d == 1:
                return max(jobDifficulty[idx:])
            (day_difficulty, total_difficulty) = (-float('inf'), float('inf'))
            for i in range(idx, len(jobDifficulty) - d + 1):
                day_difficulty = max(day_difficulty, jobDifficulty[i])
                total_difficulty = min(total_difficulty, day_difficulty + dfs(i + 1, d - 1))
            memo[idx, d] = total_difficulty
            return memo[idx, d]
        return dfs(0, d)
