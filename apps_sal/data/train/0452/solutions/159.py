class Solution:

    def _tmp(self):
        jd = jobDifficulty
        inf = 1000000000.0
        l = len(jd)
        if l < d:
            return -1

        @functools.lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(jd[i:])
            mind = inf
            maxd = 0
            for j in range(i, l - d + 1):
                maxd = max(maxd, jd[j])
                mind = min(mind, maxd + dfs(j + 1, d - 1))
            return mind
        return dfs(0, d)

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jd = jobDifficulty
        inf = 1000000000.0
        l = len(jd)
        if l < d:
            return -1
        opt = [[0] * (l - d_) + [inf] * d_ for d_ in range(d)]
        for i in range(d):
            for j in range(l - i):
                if i == 0:
                    opt[i][j] = max(jd[j:])
                    continue
                maxc = 0
                mino = inf
                for k in range(j, l - i):
                    maxc = max(maxc, jd[k])
                    mino = min(mino, maxc + opt[i - 1][k + 1])
                opt[i][j] = mino
        return opt[d - 1][0]
