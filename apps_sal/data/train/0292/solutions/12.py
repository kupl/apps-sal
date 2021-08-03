class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        vector = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        res = 0
        sm = float('inf')
        for vec in vector:
            p, q = vec
            sm = float('inf')
            for i in range(len(arr1)):
                cur = p * arr1[i] + q * arr2[i] + i
                res = max(res, cur - sm)
                sm = min(cur, sm)
        return res
