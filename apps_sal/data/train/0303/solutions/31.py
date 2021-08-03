class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            curr_max = arr[i]
            for j in range(0, k):
                index = min(n - 1, i + j)
                curr_max = max(curr_max, arr[index])
                if i + j + 1 >= n:
                    dp[i] = (n - i) * curr_max
                else:
                    dp[i] = max(dp[i], dp[i + j + 1] + (j + 1) * curr_max)
        return dp[0]
