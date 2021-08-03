class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        dp = len(arr) * [0]
        dp[0] = arr[0]
        for i in range(1, len(arr)):
            sub_max = 0
            for j in range(k):
                if j <= i:
                    sub_max = max(sub_max, arr[i - j])
                    dp[i] = max(dp[i], sub_max * (j + 1) + (dp[i - j - 1] if i - j - 1 >= 0 else 0))

        return dp[len(arr) - 1]
