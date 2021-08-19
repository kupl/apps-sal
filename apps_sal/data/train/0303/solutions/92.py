class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [float('-inf') for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            j = i - 1
            cnt = k
            while j >= 0 and cnt >= 1:
                maximum = max(arr[j:i])
                dp[i] = max(dp[i], dp[j] + maximum * (i - j))
                j -= 1
                cnt -= 1
        return dp[-1]
