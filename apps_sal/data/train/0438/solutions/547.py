from bisect import bisect_left


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if m == n:
            return n
        r = []
        r.append(0)
        r.append(n + 1)
        for i in range(n - 1, -1, -1):
            j = bisect_left(r, arr[i])
            if r[j] - arr[i] - 1 == m or arr[i] - r[j - 1] - 1 == m:
                return i
            r.insert(j, arr[i])
        return -1
