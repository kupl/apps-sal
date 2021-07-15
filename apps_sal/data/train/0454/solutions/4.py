class Solution:
     def maximumSwap(self, num):
         """
         :type num: int
         :rtype: int
         """
         import itertools
         
         # Convert num into a list of chars
         A = [c for c in str(num)]
         
         # Compute suffix max for A
         suff_max = list(itertools.accumulate(A[::-1], max))[::-1]
         
         # Compute char -> largest index in A
         last = {x : i for i, x in enumerate(A)}
 
         # Swap the first occurrence of A[i] < suff_max[i]
         for i, x in enumerate(A):
             if x < suff_max[i]:
                 A[i], A[last[suff_max[i]]] = A[last[suff_max[i]]], A[i]
                 break
 
         return int(''.join(A))
