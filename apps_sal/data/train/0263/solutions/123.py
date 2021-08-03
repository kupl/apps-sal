class Solution:
    def knightDialer(self, n: int) -> int:
        el = [[] for i in range(10)]
        el[0] = [4, 6]
        el[1] = [6, 8]
        el[2] = [7, 9]
        el[3] = [4, 8]
        el[4] = [3, 9, 0]
        el[5] = []
        el[6] = [1, 7, 0]
        el[7] = [2, 6]
        el[8] = [1, 3]
        el[9] = [2, 4]
        a = [[0 for i in range(10)] for j in range(n)]
        for i in range(10):
            a[0][i] = 1
        for i in range(1, n):
            for j in range(10):
                for x in el[j]:
                    a[i][j] = (a[i][j] + a[i - 1][x]) % (10**9 + 7)
        c = 0
        for i in range(10):
            c += a[-1][i]
        return c % (10**9 + 7)
