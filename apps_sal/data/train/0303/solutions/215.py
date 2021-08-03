class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)

        for i in range(1, len(arr) + 1):
            dp[i] = float('-inf')
            curr_max = arr[i - 1]
            for p in range(1, k + 1):
                if p > i:
                    break
                curr_max = max(curr_max, arr[i - p])
                dp[i] = max(dp[i], p * curr_max + dp[i - p])

        return dp[-1]
