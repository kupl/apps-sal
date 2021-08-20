class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        from sortedcontainers import SortedList
        n = len(arr)
        if n == m:
            return n
        s = SortedList()
        s.add(0)
        s.add(n + 1)
        for j in range(n - 1, -1, -1):
            a = arr[j]
            s.add(a)
            i = s.bisect_left(a)
            (le, ri) = (a - s[i - 1] - 1, s[i + 1] - a - 1)
            if le == m or ri == m:
                return j
        return -1
