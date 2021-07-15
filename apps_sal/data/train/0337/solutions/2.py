class Solution:
     def canCompleteCircuit(self, gas, cost):
         """
         :type gas: List[int]
         :type cost: List[int]
         :rtype: int
         """
         if not gas:
             return -1
         if len(gas) == 1:
             return 0 if gas[0] >= cost[0] else -1
         
         diff = [gas[i] - cost[i] for i in range(len(gas))]
         
         print(diff)
         
         start = []
         for i in range(len(diff)):
             if diff[i] < 0 and diff[(i + 1) % len(diff)] >= 0:
                 start.append((i + 1) % len(diff))
         
         if not start:
             start = [0]
         
         print(start)
         
         for i in start:
             bal = diff[i]
             ptr = (i + 1) % len(diff)
             while ptr != i:
                 bal += diff[ptr]
                 ptr = (ptr + 1) % len(diff)
                 if bal < 0:
                     break
             if bal >= 0:
                 return i
         return -1
             

