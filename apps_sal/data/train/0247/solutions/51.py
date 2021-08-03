class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        if len(arr) < 2:
            return -1

        n = len(arr)
        curSum = 0
        prefixSum = {0: -1}
        dp = [float('inf')] * n
        ans = float('inf')

        for i in range(n):
            curSum += arr[i]
            if curSum - target in prefixSum:
                j = prefixSum[curSum - target] + 1
                ans = min(ans, i - j + 1 + dp[j - 1])
                dp[i] = min(dp[i - 1], i - j + 1)
            else:
                dp[i] = dp[i - 1]
            prefixSum[curSum] = i

        return ans if ans < float('inf') else -1
