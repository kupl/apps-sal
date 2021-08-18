class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            curM = arr[i - 1]
            for j in range(1, min(i, k) + 1):
                curM = max(curM, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + curM * j)
        return dp[-1]
