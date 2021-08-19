class Solution:

    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        f = [None] * n
        for i in range(len(f)):
            f[i] = [float('inf')] * n
            f[i][i] = 0
        for l in range(2, n + 1):
            for i in range(0, n - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j] + max(arr[i:k + 1]) * max(arr[k + 1:j + 1]))
        return f[0][n - 1]
