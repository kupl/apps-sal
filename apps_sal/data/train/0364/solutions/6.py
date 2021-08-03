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
            temp = z % x
            for i in range(x):
                if temp == (y * i) % x:
                    return True
        if y != 0:
            temp = z % y
            for i in range(y):
                if temp == (x * i) % y:
                    return True
        return False
