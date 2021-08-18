class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if not arr:
            return 0
        n = len(arr)
        dp = [0] * n
        curr_max = arr[0]
        for i in range(k):
            curr_max = max(curr_max, arr[i])
            dp[i] = curr_max * (i + 1)

        for i in range(k, n):
            dp[i] = arr[i]
            curr_max = arr[i]
            for j in range(k):
                curr_max = max(curr_max, arr[i - j])
                dp[i] = max(dp[i], dp[i - j - 1] + curr_max * (j + 1))
        return dp[-1]
