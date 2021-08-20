class Solution:

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x > y:
            (x, y) = (y, x)
        if z < 0 or z > x + y:
            return False
        if x == 0:
            return z == y or z == 0
        if z % x == 0:
            return True
        if y % x == 0:
            return False
        a = x
        b = y % x
        while a > 1 and b > 1:
            a = a % b
            (a, b) = (b, a)
        if b == 0:
            m = a
        else:
            m = b
        if z % m == 0:
            return True
        return False
