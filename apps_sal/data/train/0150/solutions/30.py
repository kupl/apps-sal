class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        left = [0]*len(A)
        left[0] = A[0]
        for i in range(1,len(A)):
            left[i] = max(A[i],left[i-1])
        right = [0]*len(A)
        right[-1] = A[-1]
        for i in range(len(A)-2,-1,-1):
            right[i] = min(A[i],right[i+1])
        print((*left))
        print((*right))
        for i in range(1, len(A)):
            if right[i] >= left[i-1]:
                return i
        
#         N = len(A)
#         maxleft = [None] * N
#         minright = [None] * N

#         m = A[0]
#         for i in range(N):
#             m = max(m, A[i])
#             maxleft[i] = m

#         m = A[-1]
#         for i in range(N-1, -1, -1):
#             m = min(m, A[i])
#             minright[i] = m
#         print(*maxleft)
#         print(*minright)
#         for i in range(1, N):
#             if maxleft[i-1] <= minright[i]:
#                 return i

