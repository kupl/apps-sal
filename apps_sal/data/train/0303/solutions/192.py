class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n
        for i in range(n):
            currMax = arr[i]
            size = 1
            while size <= k and i - size + 1 >= 0:
                currMax = max(currMax, arr[i - size + 1])
                dp[i] = max(dp[i], (dp[i - size] if i - size >= 0 else 0) + currMax * size)
                size += 1
        return dp[-1]
