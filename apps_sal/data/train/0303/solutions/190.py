class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        current_max = 0
        dp = [0] * n
        for i in range(n):
            if i < k:
                current_max = max(current_max, arr[i])
                dp[i] = (i + 1) * current_max
            else:
                current_max = 0
                for j in range(1, k + 1):
                    current_max = max(current_max, arr[i - j + 1])
                    dp[i] = max(dp[i], dp[i - j] + current_max * j)
        return dp[-1]
