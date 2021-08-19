class Solution:

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n == 1:
            return 10
        else:
            return (self.countNumbersWithUniqueDigits(n - 1) - self.countNumbersWithUniqueDigits(n - 2)) * (11 - n) + self.countNumbersWithUniqueDigits(n - 1)
