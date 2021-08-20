class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        def prefix_sum(arr):
            lookup = {}
            dp = [float('inf')] * len(arr)
            cumsum = 0
            for (i, num) in enumerate(arr):
                cumsum += num
                if cumsum == target:
                    dp[i] = i - 0 + 1
                elif cumsum - target in lookup:
                    dp[i] = i - lookup[cumsum - target]
                lookup[cumsum] = i
                dp[i] = min(dp[i - 1], dp[i])
            return dp
        prefix = prefix_sum(arr)
        suffix = prefix_sum(arr[::-1])[::-1]
        ans = float('inf')
        for i in range(1, len(arr)):
            ans = min(ans, prefix[i - 1] + suffix[i])
        return ans if ans != float('inf') else -1
