class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = 0
        while n > 1:
            if n & 1 == 0:
                n >>= 1
                steps += 1
            else:
                if n == 3:
                    n -= 1
                else:
                    n += 1 if n & 2 else -1
                n >>= 1
                steps += 2
        return steps
