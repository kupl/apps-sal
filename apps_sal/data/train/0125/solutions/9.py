class Solution:

    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        from functools import reduce
        k = reduce(lambda x, y: x * 10 + y, b)
        return pow(a, k, 1337)
