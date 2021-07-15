# # O(nlogn)  S(n)
# class Solution:
#     def canArrange(self, arr: List[int], k: int) -> bool:
#         A = [a % k for a in arr]
#         A.sort()
#         l = 0
#         r = len(A) - 1
#         while l < len(A) and A[l] == 0:
#             l += 1
#         if l % 2 == 1:
#             return False
#         while l < r:
#             if A[l] + A[r] != k:
#                 return False
#             l += 1
#             r -= 1
#         return True
    
    
    
    
# O(n)  S(n)    
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        c = collections.Counter([i%k for i in arr])
        for j in c:
            if j == 0:
                if c[j]%2!=0: return False
            else:
                if c[j]!=c[k-j]:return False
        return True
