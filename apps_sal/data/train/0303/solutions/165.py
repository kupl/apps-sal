class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for i in range(1, len(dp)):
            maxone = 0
            for j in range(i, i - k, -1):
                if j >= 1:
                    maxone = max(maxone, arr[j - 1])
                    dp[i] = max(dp[i], dp[j - 1] + maxone * (i - j + 1))
        return dp[-1]
