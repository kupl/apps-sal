class Solution:
     def canCompleteCircuit(self, gas, cost):
         """
         :type gas: List[int]
         :type cost: List[int]
         :rtype: int
         """
         
         if len(gas) == 1:
             if cost[0] > gas[0]:
                 return -1
             else:
                 return 0
 
         sub = [g - c for (g, c) in zip(gas, cost)]
         s = 0
         e = 1
         left = sub[0]
         while e != s:
             if left >= 0:
                 left += sub[e]
                 e = (e + 1) % len(gas)
                 if e==s and left<0:
                     return -1
             else:
                 while left < 0:
                     s = (s - 1) % len(gas)
                     left += sub[s]
                     if s == (e - 1) % len(gas):
                         return -1
         return s

