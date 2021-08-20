class Solution:

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        D = {}
        (a1, a2, a3, a4) = (-2 ** 31, -2 ** 31, -2 ** 31, -2 ** 31)
        (b1, b2, b3, b4) = (2 ** 31, 2 ** 31, 2 ** 31, 2 ** 31)
        for i in range(len(arr1)):
            t = arr1[i] + arr2[i] + i
            a1 = max(a1, t)
            b1 = min(b1, t)
            t = arr1[i] + arr2[i] - i
            a2 = max(a2, t)
            b2 = min(b2, t)
            t = arr1[i] - arr2[i] - i
            a3 = max(a3, t)
            b3 = min(b3, t)
            t = arr1[i] - arr2[i] + i
            a4 = max(a4, t)
            b4 = min(b4, t)
        return max(a1 - b1, a2 - b2, a3 - b3, a4 - b4)
