class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = {}

        def recur(i, arr, k):
            if i >= len(arr):
                return 0
            if i in dp:
                return dp[i]
            (maxi, res) = (0, 0)
            for j in range(k):
                if i + j < len(arr):
                    maxi = max(maxi, arr[i + j])
                    res = max(res, maxi * (j + 1) + recur(i + j + 1, arr, k))
            dp[i] = res
            return res
        return recur(0, arr, k)
