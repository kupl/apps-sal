class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        d = [[i - 1, i + 1] for i in range(0, n + 2)]
        latest = -1
        for (i, j) in enumerate(arr):
            (a, b) = d[j]
            if d[a][1] - a == m + 1 or a - d[a][0] == m + 1 or d[b][1] - b == m + 1 or (b - d[b][0] == m + 1):
                latest = i
            if b - a == m + 1:
                latest = i + 1
            if a >= 0:
                d[a][1] = b
            if b <= n + 1:
                d[b][0] = a
        return latest
