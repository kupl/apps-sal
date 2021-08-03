class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1 for i in range(n)]

        @lru_cache(None)
        def rec(i):
            j = 1
            while(j <= d and i - j >= 0 and arr[i - j] < arr[i]):
                dp[i] = max(dp[i], 1 + rec(i - j))
                j += 1

            j = 1
            while(j <= d and i + j < n and arr[i + j] < arr[i]):
                dp[i] = max(dp[i], 1 + rec(i + j))
                j += 1
            return dp[i]
        for k in range(n):
            rec(k)
        return max(dp)
