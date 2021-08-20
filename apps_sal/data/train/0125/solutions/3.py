class Solution:

    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        b.reverse()
        p = b.pop()
        res = pow(a, p) % 1337
        while b:
            p = b.pop()
            res = pow(res, 10) % 1337
            res = res * pow(a, p) % 1337
        return res
