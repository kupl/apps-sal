class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def factorial(n):
            if n == 0:
                return 1
            m = 1
            while n > 0:
                m = m * n
                n -= 1
            return m
        ans = ""
        digits = [i + 1 for i in range(n)]
        print(("digits: ", digits))
        total = factorial(n)
        while(len(digits) > 0):
            rem = k % factorial(n - 1)
            digit = digits[(k // factorial(n - 1) + 1 * (rem > 0)) - 1]
            ans += str(digit)
            digits.remove(digit)
            k = rem
            n -= 1
        return ans
