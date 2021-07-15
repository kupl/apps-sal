class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        def search(jobs: List[int], index: int, d: int) -> int:
            if len(jobs) - index < d:
                return -1
            if (d, index) in memo:
                return memo[(d, index)]
            if d == 1:
                memo[(d, index)] = max(jobs[index:])
                return memo[(d, index)]
            result = float('inf')
            for i in range(index, len(jobs) - d + 1):
                result = min(result, max(jobs[index: i + 1]) + search(jobs, i + 1, d - 1))
            memo[(d, index)] = result
            return result
        
        memo = {}
        return search(jobDifficulty, 0, d)

