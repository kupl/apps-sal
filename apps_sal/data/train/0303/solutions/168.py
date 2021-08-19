class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n):
            cur_max = 0
            for d in range(1, min(k, i + 1) + 1):
                cur_max = max(cur_max, arr[i - d + 1])
                dp[i + 1] = max(dp[i + 1], dp[i + 1 - d] + cur_max * d)
            # print(dp)
        return dp[-1]
