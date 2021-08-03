class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # time O(n^2); space O(n)
        n = min(steps // 2 + 1, arrLen)
        dp = [0] * n
        dp[0] = 1
        for _ in range(steps):
            tmp_dp = [0] * n
            for idx in range(n):
                tmp_dp[idx] = sum(dp[max(0, idx - 1):min(n, idx + 1) + 1])
            dp = tmp_dp

        return dp[0] % (10**9 + 7)
