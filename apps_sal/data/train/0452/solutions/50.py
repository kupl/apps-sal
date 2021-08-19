class Solution:

    def minDifficulty(self, A: List[int], d: int) -> int:
        if len(A) < d:
            return -1
        dp = {}

        def dfs(i, d):
            if d == 1:
                return max(A[i:])
            if (i, d) in dp:
                return dp[i, d]
            minVal = float('inf')
            maxNow = 0
            for j in range(i, len(A) - d + 1):
                maxNow = max(maxNow, A[j])
                minVal = min(minVal, dfs(j + 1, d - 1) + maxNow)
            dp[i, d] = minVal
            return dp[i, d]
        return dfs(0, d)
