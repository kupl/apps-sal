class Solution:
     def predictPartyVictory(self, senate):
         """
         :type senate: str
         :rtype: str
         """
         from collections import deque
         n = len(senate)
         queueR = deque()
         queueD = deque()
         for i in range(len(senate)):
             if senate[i] == "R":
                 queueR.append(i)
             else:
                 queueD.append(i)
         while queueR and queueD:
             p1 = queueR.popleft()
             p2 = queueD.popleft()
             if p1 < p2:
                 queueR.append(p1+n)
             else:
                 queueD.append(p2+n)
         if queueR:
             return "Radiant"
         return "Dire"
