from sortedcontainers import SortedList


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        s = SortedList([0, n + 1])
        if n == m:
            return n
        for (i, x) in enumerate(reversed(arr)):
            j = s.bisect_left(x)
            s.add(x)
            if m == x - s[j - 1] - 1 or m == s[j + 1] - x - 1:
                return n - i - 1
        return -1
