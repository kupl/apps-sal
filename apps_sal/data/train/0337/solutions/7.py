class Solution:
     def canCompleteCircuit(self, gas, cost):
         """
         :type gas: List[int]
         :type cost: List[int]
         :rtype: int
         """
         n = len(gas)
         
         i = 0
         while i < n:
             total_gas = 0
             j = 0
             while j < n and total_gas >= 0:
                 index = (i + j) % n
                 total_gas += gas[index] - cost[index]
                 j += 1
             if total_gas >= 0:
                 return i
             while i < n and gas[i] - cost[i] >= 0:
                 i += 1
             i += 1
         
         return -1

