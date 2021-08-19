class Solution:

    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        elif len(arr) == 1:
            return arr[0]
        dp = {}
        for i in range(len(arr)):
            dp[i, i + 1] = (0, arr[i])
        for length in range(2, len(arr) + 1):
            for i in range(len(arr) - length + 1):
                end = i + length
                minSum = float('inf')
                maxLeafValue = float('-inf')
                for k in range(i + 1, end):
                    minSum = min(minSum, dp[i, k][0] + dp[k, end][0] + dp[i, k][1] * dp[k, end][1])
                    maxLeafValue = max([maxLeafValue, dp[i, k][1], dp[k, end][1]])
                dp[i, end] = (minSum, maxLeafValue)
        return dp[0, len(arr)][0]
