class Solution:
    import math

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        a = 0
        options = ''
        for i in range(n):
            options += str(i + 1)
        ans = ''
        while n > 0:
            x = math.factorial(n - 1)
            while k > x:
                k -= x
                a += 1
            ans += options[a]
            options = options[:a] + options[a + 1:]
            a = 0
            n -= 1
        return ans
