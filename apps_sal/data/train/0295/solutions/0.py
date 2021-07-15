class Solution:
     def isSelfCrossing(self, x):
         """
         :type x: List[int]
         :rtype: bool
         """
         if not x or len(x) < 4:
             return False
         i = 3
         while i < len(x):
             #print(i)
             if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                 print('case 1')
                 return True
             elif i >= 4 and x[i-1] == x[i-3] and x[i] + x[i-4] >= x[i-2]:
                 print('case 2')
                 return True
             elif i >= 5 and x[i-4] < x[i-2] <= x[i] + x[i-4] and x[i-1] <= x[i-3] <= x[i] + x[i-5]:
                 print('case 3')
                 return True
             i += 1
         return False
