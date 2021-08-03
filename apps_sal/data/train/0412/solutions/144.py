class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        A = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        A[0][0] = 1
        mod = 10 ** 9 + 7
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                for k in range(1, min(j, f) + 1):
                    A[i][j] = (A[i][j] + A[i - 1][j - k]) % mod
        return A[-1][-1]
