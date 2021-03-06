from sortedcontainers import SortedList


class Solution:

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        (workers, MOD) = (SortedList(), 10 ** 9 + 7)
        ret = ss = 0
        for (e, s) in sorted(zip(efficiency, speed), reverse=True):
            workers.add(s)
            ss += s
            if len(workers) > k:
                ss -= workers.pop(0)
            ret = max(ret, e * ss)
        return ret % MOD
