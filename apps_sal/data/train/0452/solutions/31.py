import functools
class Solution:

    def minDifficulty(self, A, d):
        n = len(A)
        if n < d: return -1

        @functools.lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(A[i:])
            res, maxd = float('inf'), 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, A[j])
                res = min(res, maxd + dfs(j + 1, d - 1))
            return res
        return dfs(0, d)

# class Solution:
#     def minDifficulty(self, A, d):
#         \"\"\"
#         :type jobDifficulty: List[int]
#         :type d: int
#         :rtype: int
#         \"\"\"
#         self.n = len(A)
#         self.A = A
#         if self.n < d: 
#             return -1
        
#         return self.dfs(0, d)
    
#     @functools.lru_cache(None)
#     def dfs(self, i, d):
#         if d == 1:
#             return max(self.A[i:])
#         res, maxd = float('inf'), 0
#         for j in range(i, self.n - d + 1):
#             maxd = max(maxd, self.A[j])
#             res = min(res, maxd + self.dfs(j + 1, d - 1))
#         return res


