class Solution:
     def sums(self, n):
         return int((n-2)*(n-1)/2)
 
     def numberOfArithmeticSlices(self, A):
         """
         :type A: List[int]
         :rtype: int
         """
         if len(A) < 3:
             return 0
         res = []
         cnt = 2
         diff = 0
         i = 1
         while i < len(A)-1:
             if i == 1:
                 diff = A[i] - A[0]
             while i < len(A) - 1 and A[i+1] - A[i] == diff:
                 cnt += 1
                 i += 1
             if cnt >= 3:
                 res.append(cnt)
             if i < len(A) - 1:
                 diff = A[i+1] - A[i]
                 cnt = 2
                 i += 1
         return sum(self.sums(x) for x in res)

