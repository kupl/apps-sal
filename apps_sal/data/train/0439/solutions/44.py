class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        i, m = 0, 0
        
        while i < len(A):
            k, last = i, 0
            while k < len(A)-1:
                if A[k] == A[k+1]:
                    break
                if A[k] > A[k+1] and last == 1:
                    break
                if A[k] < A[k+1] and last == -1:
                    break
                last = 1 if A[k] > A[k+1] else -1
                k += 1
            
            m = max(m, k-i+1)
            i = k+1 if last == 0 else k
            
        return m
        
#     def maxTurbulenceSize(self, A: List[int]) -> int:
#         i, m = 0, 0
        
#         while i < len(A):
#             k = i
#             while k < len(A)-1:
#                 if k % 2 == 1 and A[k] <= A[k+1]:
#                     break
#                 if k % 2 == 0 and A[k] >= A[k+1]:
#                     break
#                 k += 1
#             m = max(m, k - i + 1)
#             # print (i, \" \", m)
#             i = k+1
            
#         i = 0
        
#         while i < len(A):
#             k = i
#             while k < len(A)-1:
#                 if k % 2 == 1 and A[k] >= A[k+1]:
#                     break
#                 if k % 2 == 0 and A[k] <= A[k+1]:
#                     break
#                 k += 1
#             m = max(m, k - i + 1)
#             # print (i, \" \", m)
#             i = k+1
        
#         return m

