class Solution:

    def helper(self, n):
        if n == 0:
            return ['0']
        if n == 1:
            return ['0', '1']
        ret = []
        for code in self.helper(n - 1):
            ret.append('0' + code)
        for code in reversed(self.helper(n - 1)):
            ret.append('1' + code)
        return ret

    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        ret = []
        code = self.grayCode(n - 1)
        ret += code
        for v in reversed(code):
            ret.append(2 ** (n - 1) + v)
        return ret
