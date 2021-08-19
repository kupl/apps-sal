class Solution:

    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        res = [[0] * n for _ in range(n)]
        record = set()
        (rupper, rdown, cleft, cright, val) = (0, n - 1, 0, n - 1, 1)
        while rupper < rdown and cleft < cright:
            for col in range(cleft, cright):
                res[rupper][col] = val
                val += 1
            for row in range(rupper, rdown):
                res[row][cright] = val
                val += 1
            for col in range(cright, cleft, -1):
                res[rdown][col] = val
                val += 1
            for row in range(rdown, rupper, -1):
                res[row][cleft] = val
                val += 1
            rupper += 1
            rdown -= 1
            cleft += 1
            cright -= 1
        if n % 2 != 0:
            res[n // 2][n // 2] = val
        return res
