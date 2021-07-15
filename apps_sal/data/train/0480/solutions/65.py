class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # time O(n); space O(n)
        n = min(steps, arrLen)
        dp = [0] * n
        dp[0] = 1
        for step in range(1, steps+1):
            tmp_dp = [0] * n
            for idx in range(n):
                tmp_dp[idx] = sum(dp[max(0, idx-1):min(idx+1, n)+1])
            dp = tmp_dp
        
        return dp[0] % (10**9+7)
