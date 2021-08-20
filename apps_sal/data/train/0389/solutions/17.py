class Solution:

    def splitArraySameAverage(self, A: List[int]) -> bool:
        memo = {}

        def dfs(k, idx, total):
            if k == 0:
                return total == 0
            if k + idx > len(A):
                return False
            if (k, idx, total) in memo:
                return memo[k, idx, total]
            pick = dfs(k - 1, idx + 1, total - A[idx])
            not_pick = dfs(k, idx + 1, total)
            memo[k - 1, idx + 1, total - A[idx]] = pick or not_pick
            return pick or not_pick
        (n, s) = (len(A), sum(A))
        for k in range(1, n // 2 + 1):
            if k * s % n == 0 and dfs(k, 0, k * s // n):
                return True
        return False
