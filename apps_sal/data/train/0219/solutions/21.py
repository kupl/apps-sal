class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        ret = 0
        overall = 0

        totals = {}
        for i, h in enumerate(hours):
            if h > 8:
                overall += 1
            else:
                overall -= 1

            if overall > 0:
                ret = i + 1
            else:
                if overall - 1 in totals:
                    length = i - totals[overall - 1]
                    ret = max(ret, length)
                if overall not in totals:
                    totals[overall] = i

        return ret
