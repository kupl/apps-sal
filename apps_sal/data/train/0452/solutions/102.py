class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        llen = len(jobDifficulty)
        if d > llen:
            return -1
        if llen == 1:
            return jobDifficulty[0]
        dct = [[float('inf') for _ in range(d + 1)] for _ in range(llen + 1)]

        for i in range(1, llen + 1):
            for j in range(1, d + 1):
                if j == 1:
                    dct[i][1] = max(jobDifficulty[:i])
                    continue
                elif i < j:
                    continue
                for k in range(1, i):
                    dct[i][j] = min(dct[i][j], dct[k][j - 1] + max(jobDifficulty[k:i]))

        return dct[llen][d]
