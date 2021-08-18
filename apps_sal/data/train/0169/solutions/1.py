class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        import math
        if n == 2 or n == 3:
            return n - 1
        else:
            if n % 3 == 1:
                m1 = 2
            elif n % 3 == 2:
                m1 = 1
            else:
                m1 = 0
            m2 = (n - 2 * m1) // 3
            return 2**m1 * 3**m2
