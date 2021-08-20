class Solution:

    def maxAbsValExpr(self, arr1, arr2) -> int:
        res = 0
        length = len(arr1)
        for (p, q) in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
            min_v = p * arr1[0] + q * arr2[0] + 0
            for i in range(1, length):
                v = p * arr1[i] + q * arr2[i] + i
                res = max(res, v - min_v)
                min_v = min(v, min_v)
        return res
