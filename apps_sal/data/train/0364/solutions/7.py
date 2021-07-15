class Solution:
     def canMeasureWater(self, x, y, z):
         """
         :type x: int
         :type y: int
         :type z: int
         :rtype: bool
         """
         if z in [0, x, y, x + y]:
             return True
         if z > x + y or z < 0:
             return False
         if x > y:
             x, y = y, x
         if x != 0:
             for i in range(x):
                 if z % x == (y * i) % x:
                     return True
         if y != 0:
             for i in range(y):
                 if z % y == (x * i) % y:
                     return True
         return False
