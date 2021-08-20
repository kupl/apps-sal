class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * (len(arr) + 1)
        dp[1] = arr[0]
        for i in range(2, len(dp)):
            for j in range(1, k + 1):
                if i - j < 0:
                    continue
                dp[i] = max(dp[i], dp[i - j] + j * max(arr[i - j:i]))
        print(dp)
        return dp[len(arr)]
