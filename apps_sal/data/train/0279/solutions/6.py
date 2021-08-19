class Solution:

    def factorial(self, n):
        if n <= 1:
            return 1
        return self.factorial(n - 1) * n

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        r = ''
        nums = [i + 1 for i in range(n)]
        m = n
        while m:
            np = self.factorial(m - 1)
            i = (k - 1) // np
            k -= i * np
            r += str(nums[i])
            del nums[i]
            m = len(nums)
        return r
