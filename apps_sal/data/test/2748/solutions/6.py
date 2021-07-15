import queue
 class Solution:
     def letterCombinations(self, digits):
         """
         :type digits: str
         :rtype: List[str]
         """
         letterDict = {0:[],1:[],2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],
                       6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
         if len(digits) == 0:
             return []
         res = [""]
         for i in range(len(digits)):
             num = int(digits[i])
             chars = letterDict[num]
             if len(chars) == 0:
                 continue
             s = []
             for j in range(len(chars)):
                 for k in range(len(res)):
                     s.append(res[k] + chars[j])
             res = s
         return res
                     
