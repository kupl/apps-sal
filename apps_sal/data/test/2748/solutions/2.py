class Solution:
     def letterCombinations(self, digits):
         """
         :type digits: str
         :rtype: List[str]
         """
         
         dic = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], 
                '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
         
         if '0' in digits:
             digits = digits.replace('0','')
         if '1' in digits:
             digits = digits.replace('1','')
         
         count = 0
         for a in '23456789':
             if a not in digits:
                 count += 1
         if count == 8:
             return []
         
     
         res = []
         
         temp = ['']
         i = 0
         while i < len(digits):
             for a in temp:
                 for b in dic[digits[i]]:
                     res.append(a+b)
             temp = res
             res = []
             i += 1
         return temp
         
         
         
         
         

