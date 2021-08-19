class Solution:

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        def fn(x, y):
            return x * y
        import functools
        nums = list(range(1, n + 1))
        nn = functools.reduce(fn, nums)
        out = ''
        k = k - 1
        while n > 1:
            nn = nn // n
            (idx, k) = (k // nn, k % nn)
            out = out + str(nums[idx])
            nums.remove(nums[idx])
            n = n - 1
        out = out + str(nums[0])
        return out
