class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)

        res = 0
        for p, q in [[1, -1], [-1, 1], [1, 1], [-1, -1]]:
            smallest = p * arr1[0] + q * arr2[0] + 0
            for i in range(1, n):
                x = arr1[i] * p + arr2[i] * q + i
                res = max(res, x - smallest)
                smallest = min(smallest, x)
        return res
