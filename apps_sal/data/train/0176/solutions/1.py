class Solution:
 
     def __init__(self):
         self._cache = {}
 
     def isScramble(self, A, B):
 
         if (A, B) in self._cache:
             return self._cache[(A, B)]
 
         if len(A) != len(B) or sorted(A) != sorted(B):
             self._cache[(A, B)] = False
             return False
 
         if len(A) == 1 or A == B:
             self._cache[(A, B)] = True
             return True
 
         for i in range(1, len(A)):
             if self.isScramble(A[:i], B[:i]) and self.isScramble(A[i:], B[i:]):
                 self._cache[(A, B)] = True
                 return True
             elif self.isScramble(A[:i], B[-i:]) and self.isScramble(A[i:], B[:-i]):
                 self._cache[(A, B)] = True
                 return True
         self._cache[(A, B)] = False
         return False
