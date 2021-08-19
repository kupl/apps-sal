class Solution:

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        ans = 10
        d = 9
        prod = 9
        for i in range(2, n + 1):
            prod *= d
            d -= 1
            ans += prod
        return ans
