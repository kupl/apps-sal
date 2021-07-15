class Solution:
     def letterCombinations(self, digits):
         """
         :type digits: str
         :rtype: List[str]
         """
         key = {2:'abc', 3:'def', 4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
     
         nonlocal out
         out = ['']
 
         def eachLetter(i):
             if i < len(digits):
                 nonlocal out
                 if int(digits[i]) > 1:
                     x = []
                     for j in out:
                         for k in key[int(digits[i])]:
                             x.append(j+k)
                     out = x
 
                 eachLetter(i+1)
 
         eachLetter(0)
         
         return [] if out[0] is '' else out

