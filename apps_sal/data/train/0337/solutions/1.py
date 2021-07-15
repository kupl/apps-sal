class Solution:
     def canCompleteCircuit(self, gas, cost):
         """
         :type gas: List[int]
         :type cost: List[int]
         :rtype: int
         """
         if sum(gas) < sum(cost):
             return -1
         
         totalGas = 0
         position = 0
         for i in range(len(gas)):
             totalGas += gas[i] - cost[i]
             
             if totalGas < 0:
                 totalGas = 0
                 position = i + 1
         
         return position

