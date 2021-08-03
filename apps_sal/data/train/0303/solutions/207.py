class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        dp = {}

        def help(arr, k, start=0):

            if start == len(arr):
                return 0

            if start in dp:
                return dp[start]

            dp[start] = -float('inf')
            maxval = arr[start]

            for i in range(start, min(start + k, len(arr))):
                maxval = max(maxval, arr[i])
                dp[start] = max(dp[start], maxval * (i - start + 1) + help(arr, k, i + 1))

            return dp[start]

        return help(arr, k)
