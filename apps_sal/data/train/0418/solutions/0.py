class Solution:

    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        '\n         if n == 1:\n             return 0\n         if not (n & 1):\n             return self.integerReplacement(n//2) + 1\n         return min(self.integerReplacement(n+1), self.integerReplacement(n-1)) + 1\n         '
        ans = 0
        while n > 1:
            if n % 2 == 0:
                n = n // 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
            ans += 1
        return ans
