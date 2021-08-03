class Solution:
    def knightDialer(self, n: int) -> int:

        tab = [[0 for i in range(n + 1)] for i in range(10)]

        for i in range(10):
            tab[i][1] = 1

        for i in range(2, n + 1):
            for j in range(10):
                if j == 0:
                    tab[j][i] = tab[4][i - 1] + tab[6][i - 1]
                if j == 1:
                    tab[j][i] = tab[6][i - 1] + tab[8][i - 1]
                if j == 2:
                    tab[j][i] = tab[7][i - 1] + tab[9][i - 1]
                if j == 3:
                    tab[j][i] = tab[4][i - 1] + tab[8][i - 1]
                if j == 4:
                    tab[j][i] = tab[3][i - 1] + tab[9][i - 1] + tab[0][i - 1]
                if j == 5:
                    tab[j][i] = 0
                if j == 6:
                    tab[j][i] = tab[1][i - 1] + tab[7][i - 1] + tab[0][i - 1]
                if j == 7:
                    tab[j][i] = tab[2][i - 1] + tab[6][i - 1]
                if j == 8:
                    tab[j][i] = tab[1][i - 1] + tab[3][i - 1]
                if j == 9:
                    tab[j][i] = tab[2][i - 1] + tab[4][i - 1]

                tab[j][i] = tab[j][i] % (10**9 + 7)

        s = 0

        for i in range(10):
            s += tab[i][n]

        s = s % (10**9 + 7)

        return s
