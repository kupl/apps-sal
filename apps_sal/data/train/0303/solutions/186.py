class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n):
            currMax = arr[i]
            size = 1
            while size <= k and i - size + 1 >= 0:
                currMax = max(currMax, arr[i - size + 1])
                dp[i + 1] = max(dp[i + 1], dp[i + 1 - size] + (currMax * size))
                size += 1

        return dp[n]
