class Solution:
     def canCompleteCircuit(self, gas, cost):
         """
         :type gas: List[int]
         :type cost: List[int]
         :rtype: int
         """
 
         st, ed, cur, n, loop = 0, -1, 0, len(gas), False
         while True:
             ed += 1
             if ed >= n: ed -= n
             while cur + gas[ed] - cost[ed] >= 0:
                 cur += gas[ed] - cost[ed]
                 ed += 1
                 if ed >= n:
                     if loop: return -1
                     ed -= n
                     loop = True
                 if ed >= st and loop: return st
             cur, st = 0, ed + 1
             if st >= n: return -1
