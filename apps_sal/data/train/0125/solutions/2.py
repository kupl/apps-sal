class Solution:

    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        res = a ** b[0]
        for i in range(1, len(b)):
            res = res ** 10 % 1337 * a ** b[i] % 1337 % 1337
        return res
