class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        res = [[0] * (N + 1) for _ in range(K)]
        for i in range(N + 1):
            res[0][i] = i
        if K == 1:
            return N
        for k in range(1, K):
            j = 1
            for i in range(1, N + 1):
                while j < i + 1 and res[k - 1][j - 1] < res[k][i - j]:
                    j += 1
                res[k][i] = 1 + res[k - 1][j - 1]
        return int(res[K - 1][N])
