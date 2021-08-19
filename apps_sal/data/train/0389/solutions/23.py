class Solution:

    def splitArraySameAverage(self, A: List[int]) -> bool:
        memo = {}

        def dfs(total, k, idx) -> bool:
            if k == 0:
                return total == 0
            if k + idx > len(A):
                return False
            if (total, k, idx) in memo:
                return memo[total, k, idx]
            pick = dfs(total - A[idx], k - 1, idx + 1)
            not_pick = dfs(total, k, idx + 1)
            memo[total - A[idx], k - 1, idx + 1] = pick or not_pick
            return memo[total - A[idx], k - 1, idx + 1]
        (n, s) = (len(A), sum(A))
        return any((dfs(s * k // n, k, 0) for k in range(1, n // 2 + 1) if k * s % n == 0))
