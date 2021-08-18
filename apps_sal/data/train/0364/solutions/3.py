class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if not x or not y:
            return not z
        if z > x + y:
            return False

        while x != y:
            if x > y:
                x, y = x - y, y
            else:
                x, y = x, y - x

        return False if z % x else True
