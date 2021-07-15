class Solution:
     def canCompleteCircuit(self, gas, cost):
         """
         :type gas: List[int]
         :type cost: List[int]
         :rtype: int
         """
         if sum(gas) < sum(cost):
             return -1
         Rest = 0
         index = 0
         for i in range(len(gas)):
             Rest += gas[i] - cost[i]
             if Rest < 0:
                 index = i + 1
                 Rest = 0
         return index
