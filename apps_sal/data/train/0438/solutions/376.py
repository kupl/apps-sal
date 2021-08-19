class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        res = -1
        n = len(arr)
        if n == m:
            return n
        g = [0] * (n + 2)
        for (i, x) in enumerate(arr):
            l = g[x - 1]
            r = g[x + 1]
            if l == m or r == m:
                res = i
            g[x - l] = g[x + r] = l + r + 1
        return res
