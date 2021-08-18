class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        if not arr:
            return 0
        n = len(arr)
        dp = [float('inf')] * n
        presum = 0
        indexes = {0: -1}
        res = float('inf')
        for i, a in enumerate(arr):
            presum += a
            if i > 0:
                dp[i] = dp[i - 1]
            if presum - target in indexes:
                idx = indexes[presum - target]
                l = i - idx
                if dp[idx] != float('inf'):
                    res = min(res, l + dp[idx])
                dp[i] = min(dp[i], l)

            indexes[presum] = i
        return res if res < float('inf') else -1
