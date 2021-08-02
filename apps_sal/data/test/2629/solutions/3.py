class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        elif n == 1:
            return [[1]]

        cnt = 1
        ret = [[None] * n for _ in range(n)]

        def layer(width, margin):
            if not width > 0:
                return
            nonlocal cnt
            for i in range(margin, margin + width):
                ret[margin][i] = cnt
                cnt += 1
            for i in range(margin + 1, margin + width):
                ret[i][margin + width - 1] = cnt
                cnt += 1
            for i in range(margin + width - 2, margin - 1, -1):
                ret[margin + width - 1][i] = cnt
                cnt += 1
            for i in range(margin + width - 2, margin, -1):
                ret[i][margin] = cnt
                cnt += 1
            layer(width - 2, margin + 1)
        layer(n, 0)
        return ret
