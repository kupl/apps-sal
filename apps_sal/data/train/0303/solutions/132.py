class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        dp[0] = arr[0]
        for i in range(1, len(arr)):
            ans = -100000
            for z in range(max(0, i - k + 1), i + 1):
                ans = max(dp[z - 1] + max(arr[z:i + 1]) * (i - z + 1), ans)
            dp[i] = ans
        return dp[-2]
