class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        res = 0

        for p, q in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            smallest = p * arr1[0] + q * arr2[0]
            for i in range(n):
                cur = p * arr1[i] + q * arr2[i] + i
                res = max(cur - smallest, res)
                smallest = min(smallest, cur)
        return res
