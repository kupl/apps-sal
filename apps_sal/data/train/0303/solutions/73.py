class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.cache = {}

        def helper(arr, k, start):
            if start in self.cache:
                return self.cache[start]
            _arr = arr[start:]
            if len(_arr) == 0:
                return 0
            if len(_arr) <= k:
                return max(_arr) * len(_arr)
            ans = -1
            for i in range(1, k + 1):
                ans = max(ans, i * max(_arr[:i]) + helper(arr, k, start + i))
            self.cache[start] = ans
            return ans
        return helper(arr, k, 0)
