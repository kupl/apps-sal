from math import comb


class Solution:
    def ncr(self, n, r):
        sum = 0
        r = min(n, r)
        for l in range(1, r + 1):
            sum += comb(n, l)
        return sum

    def superEggDrop(self, K, N):

        matrix = [[0 for j in range(K)]for i in range(N)]
        for i in range(N):
            for j in range(K):
                matrix[i][j] = self.ncr(i + 1, j + 1)
                if matrix[i][K - 1] >= N:
                    return i + 1
        print(matrix)
