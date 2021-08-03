class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(n):
            cur = 0
            for j in range(1, min(k, i + 1) + 1):
                cur = max(cur, arr[i - j + 1])
                dp[i] = max(dp[i], cur * j + dp[i - j])
        return dp[-2]
