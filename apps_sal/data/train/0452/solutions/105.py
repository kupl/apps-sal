class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1

        return self.topdown(jobDifficulty, d, 0, {})

    def topdown(self, job, d, index, memo):
        if d <= 0:
            return flot('inf')

        if d == 1:
            if index < len(job):
                return max(job[index:])
            return float('inf')

        if (d, index) in memo:
            return memo[(d, index)]

        minDiff = float('inf')

        for i in range(index, len(job)):
            minDiff = min(minDiff, self.topdown(job, d - 1, i + 1, memo) + max(job[index:i + 1]))

        memo[(d, index)] = minDiff

        return minDiff
