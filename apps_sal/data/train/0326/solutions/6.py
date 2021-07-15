class Solution:
     def convert(self, s, numRows):
         """
         :type s: str
         :type numRows: int
         :rtype: str
         """
         if len(s) == 0 or numRows < 1:
             return ''
         if numRows == 1:
             return s
         maxStep = (numRows-1)*2
         reStr = ''
         for i in range(numRows):
             j = i
             step = maxStep-2*i
             while j < len(s):
                 reStr += s[j]
                 if step == 0:
                     j += maxStep
                 else:                    
                     j += step
                 step = maxStep-step
                 if step == 0:
                     step = maxStep
         return reStr
