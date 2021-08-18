class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        n = len(arr)

        m = [None] * n
        for i in range(len(m)):
            m[i] = [float('-inf')] * n
            m[i][i] = arr[i]
        for l in range(2, n + 1):
            for i in range(0, n - l + 1):
                j = i + l - 1
                mid = (i + j) // 2
                m[i][j] = max(m[i][j], m[i][mid], m[mid + 1][j])

        f = [None] * n
        for i in range(len(f)):
            f[i] = [float('inf')] * n
            f[i][i] = 0
        for l in range(2, n + 1):
            for i in range(0, n - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j] + m[i][k] * m[k + 1][j])
        return f[0][n - 1]
