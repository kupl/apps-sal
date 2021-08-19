class Solution:

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        points = list(zip(arr1, arr2, range(n)))
        funcs = [lambda x, y, z: x + y + z, lambda x, y, z: -x + y + z, lambda x, y, z: x - y + z, lambda x, y, z: -x - y + z]
        ans = 0
        for func in funcs:
            mapped = [func(*p) for p in points]
            ans = max(ans, max(mapped) - min(mapped))
        return ans
