class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        if len(jobs) < d:
            return -1
        
        return self.topDown(jobs, d, 0, {})
    
    def topDown(self, jobs, d, index, memo):
        if d <= 0:
            return float('inf')
        # if len(jobs) - index + 1 < d:
        #     return float('inf')
        if d == 1:
            if index < len(jobs):
                return max(jobs[index: ])
            return float('inf')
        if (d, index) in memo:
            return memo[(d, index)]
        
        mindiff = float('inf')
        
        for i in range(index, len(jobs)):
            mindiff = min(mindiff, self.topDown(jobs, d - 1, i + 1, memo) + max(jobs[index : i + 1]))
        memo[(d, index)] = mindiff
        return mindiff

