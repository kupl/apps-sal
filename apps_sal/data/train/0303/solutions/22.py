class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if arr is None or len(arr) == 0:
            return 0
        dp = [0 for _ in range(len(arr))]
        for i in range(len(arr)):
            max_elem = arr[i]
            j = 1
            while j <= k and i - j + 1 >= 0:
                max_elem = max(max_elem, arr[i - j + 1])
                if i - j >= 0:
                    dp[i] = max(dp[i], max_elem * j + dp[i - j])
                else:
                    dp[i] = max(dp[i], max_elem * j)
                j += 1
        return dp[-1]
