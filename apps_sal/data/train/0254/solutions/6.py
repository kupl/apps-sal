class Solution:

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        digits = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans = 0
        while n > 0:
            if n == 1:
                ans += 10
            else:
                res = 1
                for i in range(n):
                    res *= digits[i]
                ans += res
            n -= 1
        return ans
