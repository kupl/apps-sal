class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n
        for i in range(n):
            dp[i] = arr[i] + (dp[i - 1] if i - 1 >= 0 else 0)
            tmp = arr[i]
            for j in range(1, k):
                if i - j >= 0:
                    tmp = max(tmp, arr[i - j])
                    dp[i] = max(dp[i], tmp * (i - (i - j) + 1) + (dp[i - j - 1] if i - j - 1 >= 0 else 0))
        return dp[-1]
