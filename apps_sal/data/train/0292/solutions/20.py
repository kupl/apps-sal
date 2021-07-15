class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        res, n = 0, len(arr1)
        for x, y in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            mini = x * arr1[0] + y * arr2[0]
            for i in range(n):
                temp = x * arr1[i] + y * arr2[i] + i
                res = max(res, temp - mini)
                mini = min(mini, temp)
        return res
