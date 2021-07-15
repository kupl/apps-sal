from functools import lru_cache
class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        A.sort()
        @lru_cache(None)
        def dfs(idx, n, target):
            if target == 0 and n == 0:
                return True
            if idx >= len(A) or n == 0:
                return False
            return dfs(idx + 1, n - 1, target - A[idx]) or dfs(idx + 1, n, target)
        
        return any([dfs(0, i, (sum(A) * i) // len(A)) for i in range(1, len(A)) if (sum(A) * i) % len(A) == 0])
        

