class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [[-1] * (n + 1) for _ in range(n + 1)]

        def maxsum(i=0):
            if i >= n:
                return 0
            elif dp[i][n] != -1:
                return dp[i][n]
            else:
                mx = 0
                for j in range(i, min(i + k, n)):
                    mx = max(arr[j], mx)
                    dp[i][j] = mx * (j - i + 1)
                    dp[i][n] = max(dp[i][n], dp[i][j] + maxsum(j + 1))
                return dp[i][n]
        return maxsum()
