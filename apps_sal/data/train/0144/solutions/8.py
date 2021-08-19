class Solution:

    def minSteps(self, n):
        d = 2
        ans = 0
        while n > 1:
            while n % d == 0:
                ans += d
                n = n / d
            d = d + 1
        return ans
        '\n         :type n: int\n         :rtype: int\n         '
