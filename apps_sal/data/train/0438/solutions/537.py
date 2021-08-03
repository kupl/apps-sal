from bisect import bisect


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return n
        l = [0, n + 1]
        for i in range(n - 1, -1, -1):
            index = bisect(l, arr[i])
            front, end = l[index - 1], l[index]
            if end - front <= m:
                continue
            if arr[i] - front == m + 1 or end - arr[i] == m + 1:
                return i
            else:
                l.insert(index, arr[i])
        return -1
