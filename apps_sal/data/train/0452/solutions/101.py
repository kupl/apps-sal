class Solution:
    def dfs(self, jobDifficulty, start_day, d, memo):
        if d == 1:
            return max(jobDifficulty[start_day:])

        if (start_day, d) in memo:
            return memo[(start_day, d)]
        
        min_diff = float('inf')

        for i in range(start_day, len(jobDifficulty) - d + 1):
            min_diff = min(min_diff, max(jobDifficulty[start_day:i+1]) + self.dfs(jobDifficulty, i + 1, d - 1, memo))
        
        memo[(start_day, d)] = min_diff
        return min_diff

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1

        memo = collections.defaultdict(int)
        return self.dfs(jobDifficulty, 0, d, memo)
