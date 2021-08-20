class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        m = len(jobDifficulty)
        if m == 0 or d == 0 or d > m:
            return -1
        fmax = [[0] * m for _ in range(m)]
        fdm = [[None] * m for _ in range(d + 1)]
        for i in range(m):
            for delta in range(m - i):
                if delta == 0:
                    fmax[i][i + delta] = jobDifficulty[i]
                else:
                    fmax[i][i + delta] = max(fmax[i][i + delta - 1], jobDifficulty[i + delta])
        for mi in range(m):
            fdm[1][mi] = fmax[0][mi]
        for di in range(2, d + 1):
            for mi in range(di - 1, m - d + di):
                for ki in range(di - 2, mi):
                    if not fdm[di][mi]:
                        fdm[di][mi] = fdm[di - 1][ki] + fmax[ki + 1][mi]
                    else:
                        fdm[di][mi] = min(fdm[di][mi], fdm[di - 1][ki] + fmax[ki + 1][mi])
        return fdm[d][m - 1]
