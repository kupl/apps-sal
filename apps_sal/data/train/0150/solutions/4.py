class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        N = len(A)
        maxleft = [None] * N
        minright = [None] * N

        m = A[0]
        for i in range(N):
            m = max(m, A[i])
            maxleft[i] = m
        
        m = A[-1]
        for i in range(N -1, -1, -1):
            m = min(m, A[i])
            minright[i] = m
            
        for i in range(1, N):
            if maxleft[i-1] <= minright[i]:
                return i
            
            
#         # https://leetcode.com/problems/partition-array-into-disjoint-intervals/discuss/175904/Explained-Python-simple-O(N)-time-O(1)-space
        
#         # The idea is, v is nothing but the max value of the left half and max_so_far is a nonlocal maximum of the entire array. So by selecting elements only lesser than max of left side (v), we set V to the first element.
        
#         disjoint = 0
#         v = A[disjoint]
#         max_so_far = v
#         for i in range(len(A)):
#             max_so_far = max(max_so_far, A[i])
#             if A[i] < v: 
#                 disjoint = i
#                 v = max_so_far
#         return disjoint + 1

