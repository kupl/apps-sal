class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        retv = [[0 for i in range(n)] for j in range(n)]
        num = n * n
        i, j, di, dj = 0, 0, 0, 1
        for k in range(1, num + 1):
            retv[i][j] = k
            if retv[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di

            i += di
            j += dj

        return retv
