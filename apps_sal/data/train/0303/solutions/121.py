class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if not arr:
            return 0
        n = len(arr)
        dp = [0] * n
        for i in range(n):
            for j in range(k):
                if i - j < 0:
                    continue
                _max = max(arr[i - j:i + 1])
                _sum = _max * (j + 1) if i - j == 0 else dp[i - j - 1] + _max * (j + 1)
                dp[i] = max(dp[i], _sum)
        return dp[-1]
