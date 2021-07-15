class Solution:
   def findMinMoves(self,machines):
     s = sum(machines)
     l = len(machines)
     if s%l: return -1
     a, c, ans = int(s/l), 0, 0
     for x in machines:
       y = x - a
       c += y
       ans = max(ans, y, abs(c))
     return ans
     """
     :type machines: List[int]
     :rtype: int
     """
