class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x % y)

        if x == 0 and y == 0:
            return z == 0
        return z % gcd(x, y) == 0 and x + y >= z
