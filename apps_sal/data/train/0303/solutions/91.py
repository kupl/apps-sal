class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """Dynamic program using a list named dp, where dp[i] indicates the largest sum of the array arr[:i]."""
        dp = [0] * len(arr)
        for i in range(len(arr)):
            maxsum = 0
            for j in range(k):
                if i - j >= 1:
                    maxsum = max(maxsum, (j + 1) * max(arr[i - j:i + 1]) + dp[i - j - 1])
                elif i - j >= 0:
                    maxsum = max(maxsum, (j + 1) * max(arr[i - j:i + 1]))
            dp[i] = maxsum
        return dp[-1]
