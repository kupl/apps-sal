class Solution:

    def grayCode(self, n):
        res = []
        size = 1 << n
        for i in range(size):
            res.append(i >> 1 ^ i)
        return res
