class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        ar_len = len(arr)
        dp = [0] * (ar_len + 1)
        for i in range(1, len(dp)):
            tmp_max = []
            for j in range(1, k + 1):
                if i - j >= 0:
                    max_t = dp[i - j] + max(arr[i - j:i]) * j
                    tmp_max.append(max_t)
            dp[i] = max(tmp_max)

        return dp[-1]
