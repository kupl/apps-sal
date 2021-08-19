class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        def f(i, j, cache):
            if i == 0:
                return 0 if j < 0 else float('inf')
            if j < 0:
                return float('inf')
            m = float('inf')
            if (i, j) in cache:
                return cache[(i, j)]
            for k in range(j + 1):
                today = max(jobDifficulty[k:j + 1])
                rest = f(i - 1, k - 1, cache)
                total = today + rest
                m = min(m, total)
            # print(i,j,m)
            cache[(i, j)] = m
            return m
        sol = f(d, len(jobDifficulty) - 1, {})
        return -1 if sol == float('inf') else sol
