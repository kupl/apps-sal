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

        def gcd(a, b):
            return gcd(b, a % b) if a % b else b
        return z == 0 or z % gcd(x, y) == 0
