from sortedcontainers import SortedList


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return n
        sl = SortedList([0, n + 1])
        for i in range(n)[::-1]:
            k = arr[i]
            pos = sl.bisect(k)
            (left, right) = (sl[pos - 1], sl[pos])
            if right - k - 1 == m or k - left - 1 == m:
                return i
            sl.add(k)
        return -1
