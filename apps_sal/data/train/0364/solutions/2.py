class Solution:

    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x + y < z:
            return False
        if x == z or y == z or x + y == z:
            return True
        while y:
            (x, y) = (y, x % y)
        return not z % x
