class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        mx = 0
        for a in [1, -1]:
            for b in [1, -1]:
                sm = a * arr1[0] + b * arr2[0] + 0
                for i in range(1, len(arr1)):
                    v = a * arr1[i] + b * arr2[i] + i
                    mx = max(mx, v - sm)
                    sm = min(sm, v)
        return mx
