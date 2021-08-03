from sortedcontainers import SortedList


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return n
        sl = SortedList([0, n + 1])
        for i in range(n - 1, -1, -1):
            a = arr[i]
            up = sl.bisect(a)
            if up != len(sl) and sl[up] - a - 1 == m:
                return i
            lp = up - 1
            if lp >= 0 and a - sl[lp] - 1 == m:
                return i
            sl.add(a)
        return -1
