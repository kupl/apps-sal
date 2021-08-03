class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:

        def getValue(arr):
            return max(arr) - min(arr)
        v1 = [0] * len(arr1)
        v2 = [0] * len(arr1)
        v3 = [0] * len(arr1)
        v4 = [0] * len(arr1)

        for i in range(len(arr1)):
            v1[i] = arr1[i] + arr2[i] + i
            v2[i] = arr1[i] + arr2[i] - i
            v3[i] = arr1[i] - arr2[i] + i
            v4[i] = arr1[i] - arr2[i] - i

        return max(getValue(v1), getValue(v2), getValue(v3), getValue(v4))
