class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:

        memo = {}

        def dfs(idx, k, total) -> bool:
            # base case
            if k == 0:
                return total == 0
            if k + idx > len(A):
                return False
            if (idx, k, total) in memo:
                return memo[(idx, k, total)]

            #pick or not pick
            memo[(idx + 1, k - 1, total - A[idx])] = dfs(idx + 1, k - 1, total - A[idx]) or dfs(idx + 1, k, total)
            return memo[(idx + 1, k - 1, total - A[idx])]

        s, n = sum(A), len(A)

        # to check k*s is interger
        return any(dfs(0, k, k * s // n) for k in range(1, n // 2 + 1) if k * s % n == 0)
