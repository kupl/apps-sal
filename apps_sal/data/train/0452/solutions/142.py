class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        if d > len(jobs):
            return -1
        memo = {}
        return self.findjob(jobs, d, 0, memo)
    def findjob(self, jobs, d, index, memo):
        if d <= 0:
            return float('inf')
        if d == 1:
            if index < len(jobs):
                return max(jobs[index: ])
            return float('inf')

        if (d, index) in memo:
            return memo[(d, index)]

        mini = float('inf')
        for i in range(index, len(jobs)):
            mini = min(mini, self.findjob(jobs, d-1, i+1, memo) + max(jobs[index : i+1]))
        memo[(d, index)]  = mini
        return mini

