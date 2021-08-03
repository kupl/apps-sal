from functools import lru_cache


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        dumb = 99999999999
        lim = len(jobDifficulty)

        @lru_cache(None)
        def r(i, day):
            if day == d - 1:
                return max(jobDifficulty[i:])

            if i == lim - 1 and day < d - 1:
                return dumb

            else:

                tmp = []
                for j in range(i + 1, lim):
                    tmp.append(max(jobDifficulty[i:j]) + r(j, day + 1))

                return min(tmp)

        val = r(0, 0)
        if val > dumb:
            return -1
        return val
