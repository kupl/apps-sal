class Solution:
     def isScramble(self, A, B):
         if len(A) != len(B) or sorted(A) != sorted(B):
             return False
 
         if len(A) == 1 or A == B:
             return True
 
         for i in range(1, len(A)):
             if self.isScramble(A[:i], B[:i]) and self.isScramble(A[i:], B[i:]):
                 return True
             elif self.isScramble(A[:i], B[-i:]) and self.isScramble(A[i:], B[:-i]):
                 return True
         return False
