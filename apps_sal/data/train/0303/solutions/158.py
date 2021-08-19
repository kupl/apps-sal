class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        @lru_cache(None)
        def dp(idx):
            if idx < 0:
                return 0
            left = max(idx - k + 1, 0)
            curr_max = arr[idx]
            res = arr[idx]
            for i in range(idx, left - 1, -1):
                curr_max = max(curr_max, arr[i])
                res = max(res, dp(i - 1) + (idx - i + 1) * curr_max)
            return res
        return dp(len(arr) - 1)
