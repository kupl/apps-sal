class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # dp problem
        # arr[i:j] can be split into arr[i:k] and arr[k:j]
        # min_sum of arr[i:j] is min_sum(arr[i:k]) + min_sum(arr[k:j]) + max(arr[i:k]) * max(arr[k:j])
        # max of arr[i:j] is max(max(arr[i:k]), max(arr[k:j]))
        # dp[i][j] maintains min_sum and max value
        if len(arr) == 0:
            return 0
        elif len(arr) == 1:
            return arr[0]
        dp = {}
        for i in range(len(arr)):
            dp[(i, i + 1)] = (0, arr[i])
        for length in range(2, len(arr) + 1):
            for i in range(len(arr) - length + 1):
                # calculate the solution for arr[i: i+length]
                end = i + length
                minSum = float('inf')
                maxLeafValue = float('-inf')
                for k in range(i + 1, end):
                    # pick [i: k] left tree and [k: end] as right tree
                    minSum = min(minSum, dp[(i, k)][0] + dp[(k, end)][0] + dp[(i, k)][1] * dp[(k, end)][1])
                    maxLeafValue = max([maxLeafValue, dp[(i, k)][1], dp[(k, end)][1]])
                dp[(i, end)] = (minSum, maxLeafValue)

        return dp[(0, len(arr))][0]
