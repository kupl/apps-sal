class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        self.dp = {}

        def recur(index, arr, k):
            if index >= len(arr):
                return 0
            if index in self.dp:
                return self.dp[index]
            maxi = 0
            res = 0
            for i in range(k):
                if index + i < len(arr):
                    maxi = max(maxi, arr[index + i])
                    res = max(res, maxi * (i + 1) + recur(index + i + 1, arr, k))
            self.dp[index] = res
            return res
        return recur(0, arr, k)
