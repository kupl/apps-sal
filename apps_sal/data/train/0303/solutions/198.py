class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [-1] * (len(arr) + 1)
        dp[0] = 0
        for i in range(len(arr)):
            cur_max = -1
            for j in range(k):
                if i - j < 0:
                    dp[i + 1] = max(dp[i + 1], arr[i])
                    break
                cur_max = max(cur_max, arr[i - j])
                dp[i + 1] = max(dp[i + 1], dp[i - j] + cur_max * (j + 1))
        return dp[-1]
