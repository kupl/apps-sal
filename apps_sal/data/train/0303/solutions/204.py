class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if not arr:
            return 0
        n = len(arr)
        dp = [0 for _ in range(n)]
        for i in range(n):
            temp_max = arr[i]
            j = 1
            while i - j + 1 >= 0 and j <= k:
                temp_max = max(temp_max, arr[i - j + 1])
                if i >= j:
                    dp[i] = max(dp[i], dp[i - j] + (temp_max * j))
                else:
                    dp[i] = max(dp[i], temp_max * j)
                j += 1
        return dp[-1]
