class Solution:
     def letterCombinations(self, digits):
         """
         :type digits: str
         :rtype: List[str]
         """
         if '' == digits: 
             return []
         
         kvmaps = {
             '2': 'abc',
             '3': 'def',
             '4': 'ghi',
             '5': 'jkl',
             '6': 'mno',
             '7': 'pqrs',
             '8': 'tuv',
             '9': 'wxyz'
         }
         rst = ['']
         for digit in digits:
             temp = [s + c for s in rst for c in kvmaps[digit]]
             rst = temp
         
         return rst

