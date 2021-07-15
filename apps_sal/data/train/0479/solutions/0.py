class Solution:
     def leastBricks(self, wall):
         """
         :type wall: List[List[int]]
         :rtype: int
         """
         d = {}
         for i in wall:
             suma = 0
             for j in range(len(i)-1):
                 suma += i[j]
                 if suma in d:
                     d[suma] += 1
                 else:
                     d[suma] = 1
         if len(d) == 0:
             return len(wall)
         return len(wall) - max(d.values())

