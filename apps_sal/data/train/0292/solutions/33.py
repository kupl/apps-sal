class Solution:

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        for i in range(n):
            (arr1[i], arr2[i]) = (arr1[i] + arr2[i], arr1[i] - arr2[i])
        arr11 = [x + i for (i, x) in enumerate(arr1)]
        arr12 = [x - i for (i, x) in enumerate(arr1)]
        arr21 = [x + i for (i, x) in enumerate(arr2)]
        arr22 = [x - i for (i, x) in enumerate(arr2)]
        return max((max(a) - min(a) for a in [arr11, arr12, arr21, arr22]))
