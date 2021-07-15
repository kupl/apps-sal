class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        @lru_cache(maxsize=None)
        def helper(start, end):
            if start + 1 == end:
                return 0
            
            result = 0
            for k in range(start + 1, end):
                result = min(float('inf') if result == 0 else result,
                            helper(start, k) +
                            A[start] * A[k] * A[end] +
                            helper(k, end))
            return result
        return helper(0, len(A) - 1)
