class Solution:
     
     def firstMissingPositive(self, nums):
         """
         :type nums: List[int]
         :rtype: int
         """
         A=nums
         n = len(A)
         for index in range(n):
             element = A[index]
             while True:
                 if element <= 0 or element > n or element == A[element - 1]:
                     break
                 A[element - 1], element = element, A[element - 1]
         for index in range(n):
             if A[index] != index + 1:
                 return index + 1
         return n + 1
             

