class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        m = len(A)
        total = sum(A)
        target = total / m
        A.sort()

        @lru_cache(None)
        def dfs(k, i, sum_b):
            if k == 0:
                return sum_b == 0
            if i == len(A):
                return False
            return dfs(k - 1, i + 1, sum_b - A[i]) or dfs(k, i + 1, sum_b)

        for k in range(1, m // 2 + 1):
            if total * k % m == 0:
                if dfs(k, 0, total * k // m):
                    return True
        return False
