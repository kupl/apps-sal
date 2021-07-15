# from functools import lru_cache
# class Solution:
#     def splitArraySameAverage(self, A: List[int]) -> bool:
#         # A.sort(reverse=True)
#         n, total = len(A), sum(A)
#         avag = total/n
#         # epsilon = 0.000001
#         # print(avag)
#         @lru_cache(None)
#         def dfs(idx, sums, sz):
#             if 0 < sz <= n//2 and total*sz%n == 0 and sums == total*sz//n:
#                 return True
#             if idx == n or sz > n//2 or sums > total/2:
#                 return False
            
#             return dfs(idx+1, sums+A[idx], sz+1) or dfs(idx+1, sums, sz)
#             # print(idx,sums,sz,res)
#         return dfs(0,0,0)

from functools import lru_cache
class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        n, total = len(A), sum(A)
        @lru_cache(None)
        def dfs(idx, target, sz):
            if sz == 0:
                return target == 0
            if target < 0 or idx+sz > n:
                return False
            
            
            
            return dfs(idx+1, target-A[idx], sz-1) or dfs(idx+1, target, sz)
            # print(idx,sums,sz,res)
        return any(dfs(0,total*k//n,k) for k in range(1,n//2+1) if total*k%n == 0)
