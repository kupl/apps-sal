from functools import lru_cache

class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        # TLE
#         avg = sum(A) / len(A)
#         for k in range(1, len(A) // 2 + 1):
#             for comb in combinations(A, k):
#                 if abs(sum(comb) / k - avg) < 1e-5:
#                     return True
            
#         return False

        N, S = len(A), sum(A)
        
        @lru_cache(None)
        def combinationSum(target, start, k):
            if target == 0:
                return k == 0
            if start == N or k < 0 or target < 0:
                return False
            
            return combinationSum(target-A[start], start+1, k-1) or combinationSum(target, start+1, k)
        
        for k in range(1, N // 2 + 1):
            if S * k % N == 0:
                if combinationSum(S * k // N, 0, k):
                    return True
        
        return False
