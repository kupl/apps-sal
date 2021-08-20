class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        A = arr
        dp = [0] * (n := len(arr))
        dp[0] = curr_max = arr[0]
        for i in range(1, k):
            curr_max = max(curr_max, A[i])
            dp[i] = (i + 1) * curr_max
        for i in range(k, n):
            curr_max = A[i]
            for j in range(k):
                curr_max = max(curr_max, A[i - j])
                dp[i] = max(dp[i], dp[i - j - 1] + curr_max * (j + 1))
        return dp[-1]
