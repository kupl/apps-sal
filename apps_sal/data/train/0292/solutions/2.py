class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        points = list(zip(arr1, arr2, range(n)))
        funcs = [lambda x, y, i: x + y + i,
                 lambda x, y, i: x - y - i,
                 lambda x, y, i: x - y + i,
                 lambda x, y, i: x + y - i]
        res = 0
        for func in funcs:
            temp = [func(*pt) for pt in points]
            res = max(res, max(temp)-min(temp))
        return res
