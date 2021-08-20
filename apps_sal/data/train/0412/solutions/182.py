class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        a = [[0] * (d + 1) for _ in range(target + 1)]
        a[0][0] = 1
        for i in range(1, target + 1):
            for j in range(1, d + 1):
                for k in range(1, f + 1):
                    if i >= k and j >= 1:
                        a[i][j] = (a[i][j] + a[i - k][j - 1]) % (10 ** 9 + 7)
        return a[target][d]
