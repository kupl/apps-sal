class Solution:

    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)

        @lru_cache(None)
        def max_cache(a, b):
            return max(arr[a:b])

        @lru_cache(None)
        def dp(i, j):
            n = j - i
            if n == 1:
                return 0
            if n == 2:
                return arr[i] * arr[j - 1]
            min_out = 2 ** 31 - 1
            for k in range(i + 1, j):
                min_out = min(min_out, max_cache(i, k) * max_cache(k, j) + dp(i, k) + dp(k, j))
            return min_out
        return dp(0, n)
