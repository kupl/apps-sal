class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        points = list(zip(arr1, arr2, list(range(n))))

        funcs = [
            lambda x, y, z: x + y + z,
            lambda x, y, z: x + y - z,
            lambda x, y, z: x - y + z,
            lambda x, y, z: x - y - z,
        ]

        result = 0
        for func in funcs:
            mapped = [func(*p) for p in points]
            result = max(result, max(mapped) - min(mapped))

        return result
