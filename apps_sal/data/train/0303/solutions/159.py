class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        dp = [0] * (N + 1)
        for i in range(N):
            cur_max = 0
            for j in range(1, min(k, i + 1) + 1):
                cur_max = max(cur_max, arr[i - j + 1])  # 从当前元素开始
                dp[i] = max(dp[i], dp[i - j] + cur_max * j)
        return dp[N - 1]
