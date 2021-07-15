class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if d > n:
            return -1
        dp = [[-1 for _ in range(d+1)] for _ in range(n)]
        return self.helper(jobDifficulty, n, 0, d, dp)
    
    def helper(self, jobDifficulty, n, idx, d, dp):
        if idx == n and d == 0:
            return 0
        if idx == n or d == 0:
            return float('inf')
        if dp[idx][d] != -1:
            return dp[idx][d]
        minDiff = float('inf')
        currMax = jobDifficulty[idx]
        for j in range(idx, n):
            currMax = max(currMax, jobDifficulty[j])
            temp = self.helper(jobDifficulty, n, j+1, d-1, dp)
            minDiff = min(minDiff, temp + currMax)
        dp[idx][d] = minDiff
        return minDiff

