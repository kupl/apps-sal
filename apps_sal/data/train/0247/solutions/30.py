class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        dp = [len(arr) + 1] * len(arr)
        table = {0: -1}
        s = 0
        min_sum = len(arr) + 1
        for i in range(len(arr)):
            s += arr[i]
            if i > 0:
                dp[i] = dp[i - 1]
            if s - target in table:
                length = i - table[s - target]
                dp[i] = min(dp[i], length)
                if length <= i:
                    min_sum = min(min_sum, length + dp[i - length])

            table[s] = i

        if min_sum == len(arr) + 1:
            return -1
        else:
            return min_sum
