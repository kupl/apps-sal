class Solution:

    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        memo = {}

        def solve(i, j, k):
            if k == 0:
                return 0
            elif i > j:
                return 0
            elif (i, j, k) in memo:
                return memo[i, j, k]
            memo[i, j, k] = max(slices[i] + solve(i + 2, j, k - 1), solve(i + 1, j, k))
            return memo[i, j, k]
        return max(solve(0, n - 2, n // 3), solve(1, n - 1, n // 3))
