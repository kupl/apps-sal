class Solution:

    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:

        def f1(i):
            return arr1[i] + arr2[i] + i

        def f2(i):
            return -arr1[i] + arr2[i] + i

        def f3(i):
            return arr1[i] - arr2[i] + i

        def f4(i):
            return -arr1[i] - arr2[i] + i
        res = 0
        for f in [f1, f2, f3, f4]:
            low = float('inf')
            high = -float('inf')
            for i in range(len(arr1)):
                low = min(low, f(i))
                high = max(high, f(i))
            res = max(res, high - low)
        return res
