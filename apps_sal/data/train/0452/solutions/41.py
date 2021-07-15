class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        dp = [[-1 for _ in range(d+1)] for _ in range(len(jobDifficulty))]
        return self.helper(jobDifficulty, 0, d, dp)
    
    def helper(self, jobDifficulty, idx, d, dp):
        if idx == len(jobDifficulty) and d == 0:
            return 0
        if idx == len(jobDifficulty) or d == 0:
            return float('inf')
        if dp[idx][d] != -1:
            return dp[idx][d]
        minDiff = float('inf')
        currMax = jobDifficulty[idx]
        for j in range(idx, len(jobDifficulty)):
            currMax = max(currMax, jobDifficulty[j])
            temp = self.helper(jobDifficulty, j+1, d-1, dp)
            minDiff = min(minDiff, temp + currMax)
        dp[idx][d] = minDiff
        return minDiff

