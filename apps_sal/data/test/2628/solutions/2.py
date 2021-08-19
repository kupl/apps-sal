class Solution:

    def grayCode(self, n):
        if n == 0:
            return [0]
        concat = ''
        res = [0, 1]
        for i in range(1, n):
            newRes = []
            for j in res:
                newRes.append(j)
            for j in reversed(res):
                newRes.append(j + 2 ** i)
            res = newRes
        return res
        '\n         :type n: int\n         :rtype: List[int]\n         '
