class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:

        memo = {}

        def dfs(idx, k, total) -> bool:

            if k == 0:
                return total == 0
            if idx + k > len(A):
                return False
            if (idx, k, total) in memo:
                return memo[(idx, k, total)]

            memo[(idx + 1, k - 1, total - A[idx])] = dfs(idx + 1, k - 1, total - A[idx]) or dfs(idx + 1, k, total)

            return memo[(idx + 1, k - 1, total - A[idx])]

        s, n = sum(A), len(A)
        return any(dfs(0, k, k * s // n) for k in range(1, n // 2 + 1) if k * s % n == 0)
