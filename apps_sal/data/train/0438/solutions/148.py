class Solution:

    def findLatestStep(self, arr, m):
        n = len(arr)
        if n == m:
            return m
        size = [0] * (n + 2)
        res = -1
        for (i, x) in enumerate(arr):
            if size[x - 1] == m or size[x + 1] == m:
                res = i
            size[x - size[x - 1]] = size[x + size[x + 1]] = size[x - 1] + size[x + 1] + 1
        return res
