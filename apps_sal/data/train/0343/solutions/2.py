class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_square(n):
            return int(n**0.5) * int(n**0.5) == n

        if is_square(n):
            return 1
        for i in range(1, int((n**0.5) + 1)):
            if is_square(n - i * i):
                return 2
        while (n & 3) == 0:
            n >>= 2
        if n & 7 == 7:
            return 4
        return 3
