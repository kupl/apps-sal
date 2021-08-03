class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        return self.top_down(jobDifficulty, d, 0, {})

    def top_down(self, jobs, d, index, memo):
        if d <= 0:
            return float('inf')
        if d == 1:
            if index < len(jobs):
                return max(jobs[index:])
            return float('inf')
        if (d, index) in memo:
            return memo[(d, index)]
        min_diff = float('inf')
        for i in range(index, len(jobs)):
            min_diff = min(min_diff, self.top_down(jobs, d - 1, i + 1, memo) + max(jobs[index:i + 1]))
        memo[(d, index)] = min_diff
        return min_diff
