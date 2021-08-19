class Solution:

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        while n % 4 == 0:
            n = n / 4
        if n % 8 == 7:
            return 4
        if round(math.sqrt(n)) ** 2 == n:
            return 1
        for i in range(1, math.ceil(math.sqrt(n))):
            res = n - i ** 2
            print(('i:,res:,', i, res))
            if round(math.sqrt(res)) ** 2 == res:
                return 2
        return 3
