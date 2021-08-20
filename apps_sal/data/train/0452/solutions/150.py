class Solution:

    def minDifficulty(self, jobsd: List[int], d: int) -> int:

        @lru_cache(maxsize=None)
        def cut(st, days):
            if st == len(jobsd) or days == 0 or len(jobsd) - st < days:
                return math.inf
            if days == 1:
                return max(jobsd[st:])
            (maxsofar, res) = (-math.inf, math.inf)
            for i in range(st, len(jobsd) - 1):
                maxsofar = max(maxsofar, jobsd[i])
                res = min(res, maxsofar + cut(i + 1, days - 1))
            return res
        res = cut(0, d)
        return -1 if res == math.inf else res
