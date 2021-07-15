class Solution:
    def dfs(self, jobDifficulty, start_day, d, memo):
        if d == 1:
            return max(jobDifficulty[start_day:])

        if (start_day, d) in memo:
            return memo[(start_day, d)]
        
        min_diff = float('inf')
        cur_max_diff = 0

        for i in range(start_day, len(jobDifficulty) - d + 1):
            cur_max_diff = max(cur_max_diff, jobDifficulty[i])
            min_diff = min(min_diff, cur_max_diff + self.dfs(jobDifficulty, i + 1, d - 1, memo))
        
        memo[(start_day, d)] = min_diff
        return min_diff

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1

        memo = collections.defaultdict(int)
        return self.dfs(jobDifficulty, 0, d, memo)

