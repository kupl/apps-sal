class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        if not arr:
            return 0

        if n == 1:
            return arr[0]

        if n < k:
            return sum(arr)

        dp = [0] * (n)

        for i in range(n):
            for j in range(i, max(-1, i - k), -1):
                dp[i] = max(dp[i], max(arr[j:i + 1]) * (i - j + 1) + (dp[j - 1] if j - 1 >= 0 else 0))
        return dp[-1]
